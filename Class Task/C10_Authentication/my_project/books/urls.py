from django.contrib import admin
from django.urls import path
from . import views
from books.views import MyView, BookListView, ContactFormView , BookFormView
from django.shortcuts import render
from django.contrib.auth import views as auth_views

urlpatterns = [
path('initial_class/',MyView.as_view()),
path('list/',BookListView.as_view(),name = 'list'),
path('contact/add/',ContactFormView.as_view()),
path('book/add/',BookFormView.as_view()),
path('contact/success/', lambda request: render(request, 'success/contact_success.html'), name = 'contact_success'),
path('contact/booksuccess/', lambda request: render(request, 'success/book_success.html'), name = 'book_success'),
path('test/',views.test),
path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('register/', views.register, name='register'),
# path('', views.home,name="home"),
]