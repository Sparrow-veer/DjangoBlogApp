from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','fruit_pic']
