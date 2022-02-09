from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,DOBDetail


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    dob=forms.DateField()
    location=forms.CharField()
    class Meta:
        model=User
        fields=['username','email','password1','password2','dob','location']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']


class DOBUpdateForm(forms.ModelForm):
    dob=forms.DateField()
    location=forms.CharField()

    class Meta:
        model=DOBDetail
        fields=['dob','location']
