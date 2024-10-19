
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from django.views.generic import ListView
from book.models import Book
def home(request):
    return HttpResponse("Welcome to django")

def test(request):
    return render(request,'test.html')

class MyView(View):
    def get(self, request):
        return HttpResponse("welcome to django views by class")
    
class BookListView(ListView):
    model = Book
    template_name= "book_list.html"
    context_object_name="books"