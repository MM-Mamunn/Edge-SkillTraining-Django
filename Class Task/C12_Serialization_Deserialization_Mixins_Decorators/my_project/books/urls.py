from django.contrib import admin
from django.urls import path
from . import views
from books.views import (
    BookGetUpdateDelete, MyView, BookListView, ContactFormView , BookFormView,
    BookListCreate)
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
path('home/', views.home,name="home"),
path('rest_booklist/', BookListCreate.as_view(), name='rest_book_list'),
path('rest/book/<int:pk>', BookGetUpdateDelete.as_view(), name='rest_book'),
]