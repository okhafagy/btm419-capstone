from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Product

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Enter Username',
            'class':'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class':'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Enter Username',
            'class':'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Email',
            'class':'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class':'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password Again',
            'class':'w-full py-4 px-6 rounded-xl'
    }))

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=255, label="Product Name")
    price = forms.DecimalField(
        max_digits=10000, 
        decimal_places=1, 
        label="Price",
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Price ($)', 'step': '1.00'})
    )
    
    product_image = forms.ImageField(label="Product Image")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']
        widgets = {
            'price': forms.NumberInput(attrs={'step': '0.1'}),
        }