from typing import Any
from django import forms
# from . models import Author,Publisher
from . models import Book
class ContactForm(forms.Form):
    name = forms.CharField(max_length= 200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) # widget for it is a text field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email is not from "@example.com" domain.')
        return email
    # def clean_message(self):
    #     message = self.cleaned_data.get('message')
    #     if not len(message):
    #         raise forms.ValidationError('message can nott be empty.')
    #     return message
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_date', 'price','author','publisher']
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0.0:
            raise forms.ValidationError('Price Can not be negative')
        return price
    
