from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Userprofile
from .validator import validate_unique_email

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True, validators=[validate_unique_email])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['company_image', 'company_whatsapp_number', 'company_address', 'about', 'state', 'lga', 'website' ]
        widgets = {
            'company_image': forms.ClearableFileInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl'}),
            'company_whatsapp_number': forms.TextInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl','placeholder':'Eg:+2348161728112'}),
            'website':forms.TextInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl'}),
            'state': forms.Select(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl'}),
            'lga': forms.TextInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl'}),
            'company_address': forms.TextInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl'}),
            'about': forms.Textarea(attrs={'class': 'w-full mt-2 py-4 px-6 bg-gray-100 rounded-xl','placeholder':'Make your customers know you, tell us about your company'}),

        }


