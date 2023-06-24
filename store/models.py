from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image
from io import BytesIO
from django.utils.text import slugify
from random import randint



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Category/Industry'
        ordering = ('title',)


class Subcategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Subcategories'
        ordering = ('category',)



class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waiting_approval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Waiting Approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    userprofile = models.ForeignKey('userprofile.Userprofile', related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='uploads/product_images', null=True)
    image_2 = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    image_3 = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    image_4 = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnail', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self): 
        return self.title

    


    # a method used to create a unique slug
    def save(self, *args, **kwargs):
        if Product.objects.filter(title=self.title).exists():
            extra = str(randint(1, 1000000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


    #to automatically generate a thumbnail based on the image 
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return '/media/uploads/product_images/image-unavailable.png'
            





    #to generate a thumbnail
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        #img.save(thumb_io, 'JPEG', quality=85)
        img.save(thumb_io, 'PNG', quality=85)
        name = image.name.replace('uploads/product_images/', '')
        thumbnail = File(thumb_io, name=name)

        return thumbnail




'''class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField()
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name
    
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)'''

    



    