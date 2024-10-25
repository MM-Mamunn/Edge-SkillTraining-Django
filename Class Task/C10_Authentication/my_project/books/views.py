
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from books.models import Book
from books.forms import ContactForm, BookForm
from django.views.generic.edit import CreateView
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

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url=reverse_lazy('contact_success')

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

class BookFormView(CreateView):
    model = Book                      # Specify the model to use
    form_class = BookForm             # Use the custom form we created
    template_name = 'book.html'  # Template to render the form
    success_url = reverse_lazy('list')  # Redirect after successful form submission
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})