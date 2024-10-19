from django.contrib import admin
from django.urls import path
from . import views
from book.views import MyView, BookListView 

urlpatterns = [
path('initial_class/',MyView.as_view()),
path('list/',BookListView.as_view()),
path('test/',views.test),
# path('', views.home,name="home"),
]