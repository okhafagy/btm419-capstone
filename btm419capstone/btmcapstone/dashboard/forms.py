from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_number', 'dealership', 'product', 'quantity', 'expected_delivery_date', 'actual_delivery_date']


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

