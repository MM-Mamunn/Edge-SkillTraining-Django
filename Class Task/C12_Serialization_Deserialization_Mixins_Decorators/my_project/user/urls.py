from django.contrib import admin
from django.urls import path
from . import views
from books.views import MyView, BookListView, ContactFormView , BookFormView
from django.shortcuts import render
from django.contrib.auth import views as auth_views

urlpatterns = [
path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('register/', views.register, name='register'),
]