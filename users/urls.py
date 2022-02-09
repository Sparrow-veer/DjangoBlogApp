from django.urls import path
from . import views

urlpatterns=[
    path('',views.Validation.as_view(),name='register'),
    path('profile/',views.profile,name='profile')
]