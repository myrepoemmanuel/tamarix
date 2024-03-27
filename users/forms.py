from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class LoginForm(ModelForm):
    # required_css_class = 'required'
    email = forms.EmailField()

    class Meta:
        model = User
        # fields = ['email', 'name', 'price', 'Brand', 'description', 'digital', 'image', 'image2', 'image3', 'image4']
        fields = '__all__'
        # exclude = ("vendor",)