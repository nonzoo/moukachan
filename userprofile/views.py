import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login 
from .models import Userprofile
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from .form import SignUpForm, EditAccountForm
from store.forms import ProductForm
from store.models import Product,Subcategory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .validator import validate_unique_email



def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(user__userprofile__is_vendor=True, status = Product.ACTIVE)
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'userprofile/vendor_detail.html', {
        'user':user,
        'products':products

    })




@login_required
def my_store(request):
    if request.user.userprofile.is_vendor:
        products = request.user.products.exclude(status=Product.DELETED)
        
        paginator = Paginator(products, 8)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)

        except EmptyPage:
            products = paginator.page(paginator.num_pages)


        return render(request, 'userprofile/my_store.html', {
            'products': products
        })
    else:
        return render(request, 'userprofile/create_subscription.html')

'''def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'userprofile/my_store_order_detail.html',{
        'order':order
    })
'''



def create_subscription(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    userprofile = Userprofile.objects.get(user=request.user)
    
    # Check if the user is already a vendor
    if userprofile.is_vendor:
        return redirect('userprofile/error')
    
    # Process payment and subscription creation logic with Interswitch here
    # Replace the following code with your actual payment gateway integration logic

    # Generate the payment request payload
    payload = {
        'amount': 10000,  # Replace with the actual subscription amount
        'currency': 'NGN',
        'reference': 'SUBSCRIPTION_REF',  # Replace with a unique reference for each subscription
        'email': userprofile.company_email,
        # Include other required parameters based on the Interswitch API documentation
        # ...
    }

    # Make a POST request to the Interswitch API for payment processing
    response = requests.post('https://api.interswitch.com/v2/payments', json=payload)

    if response.status_code == 200:
        # Payment was successful
        # Update the user's is_vendor field to True
        userprofile.is_vendor = True
        userprofile.save()
        messages.success(request, 'Subscription created successfully.')
        return redirect('userprofile/success')
    else:
        # Payment failed
        messages.error(request, 'Subscription creation failed.')
        return redirect('userprofile/error')
    
def success(request):
    return render(request, 'userprofile/success.html')

def error(request):
    return render(request, 'userprofile/error.html')




#for vendors to add product
@login_required
def add_product(request):

    #saving the product to the database when the submit button is clicked 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            messages.success(request, 'The product was added successfully!')

            #redirectng the vendor back to the store page after submitting the product form
            return redirect('my_store')
    
    else:
        form = ProductForm()

    return render(request, 'userprofile/product_form.html',{
        'title': 'Add product',
        'form':form
    })

#An edit function for the vendors
@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved!')

            return redirect('my_store')
            
    else:
        form = ProductForm(instance=product)


    return render(request, 'userprofile/product_form.html',{

        'title': 'Edit product',
        'product':product,
        'form':form
    })
from django.http import JsonResponse



def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'title')

    return JsonResponse({'subcategories': list(subcategories)})


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'The product was deleted!')
    return redirect('my_store')
    


@login_required
def myaccount(request):
    return render (request, 'userprofile/myaccount.html')

@login_required
def edit_account(request):
    user_profile = request.user.userprofile 
    
    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=user_profile)
        
        if form.is_valid():
            form.save()
            return redirect('myaccount')
    else:
        form = EditAccountForm(instance=user_profile)
    
    return render(request, 'userprofile/edit_account.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile = Userprofile.objects.create(user=user)
            return redirect('frontpage')
    else:
      form = SignUpForm()

    return render(request, 'userprofile/signup.html',{
        'form':form
    })



def privacy(request):
    return render(request, 'userprofile/privacy.html')

