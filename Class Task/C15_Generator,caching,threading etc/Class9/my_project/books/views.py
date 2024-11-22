from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import permission_required


#from books app
from books.forms import ContactForm, BookForm
from books.models import Book

#from rest framework
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from books.serializers import BookSerializer

def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Welcome to {request.user.username}")
    else:
        context = {'x':1}
        return render(request,'login.html',context)

def test(request):
    return render(request,'test.html')

class MyView(View):
    def get(self, request):
        return HttpResponse("welcome to django views by class")
    
class BookListView(ListView):
    model = Book
    template_name= "book_list.html"
    context_object_name="books"

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url=reverse_lazy('contact_success')

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    
@permission_required('books.can_enter_book', raise_exception=True)
def Book_entry(request):
    return render(request, 'special_page.html')

class BookFormView(CreateView):
    model = Book                      # Specify the model to use
    form_class = BookForm             # Use the custom form we created
    template_name = 'book.html'  # Template to render the form
    success_url = reverse_lazy('list')  # Redirect after successful form submission
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

#Rest framework API's
class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class BookGetUpdateDelete(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    http_method_names = ('get', 'post', 'put','delete')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 