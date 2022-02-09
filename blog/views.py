from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from . import models
import random
import requests
import asyncio

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
import logging

logging.basicConfig(filename='logfile.txt',level=logging.DEBUG)
posts=[
    {'author':'Shiv',
     'title':'the Creator',
     'content':'first content',
     'date_posted':'20-09-1998'},
    {'author':'Laxman',
     'title':'the Brother',
     'content':'second content',
     'date_posted':'10-11-1994'}
]
def home(request):
    content={
        'posts':models.Post.objects.all(),
        'title':'Authors Blog'
    }
    return render(request,'blog/home.html',content)

def about(request):
    return render(request,'blog/about.html')




class PostListView(ListView):
    model=models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model=models.Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=models.Post
    fields=['title','content','fruit_pic']


    def form_valid(self, form):
        if(len(form.instance.content)==0):
            response= requests.get("https://zenquotes.io/api/random")
            print(response)
            form.instance.content =response.json()[0]['q']

        logging.debug(self.request.user)
        logging.debug(self.request.user.email)
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=models.Post
    fields=['title','content','fruit_pic']

    def form_valid(self, form):
        if (len(form.instance.content) == 0):
            response = requests.get("https://zenquotes.io/api/random")
            print(response)
            form.instance.content = response.json()[0]['q']

        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=models.Post
    success_url = '/blog/'
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False


class UserPostListView(ListView):
    model=models.Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return models.Post.objects.filter(author=user).order_by('-date_posted')

