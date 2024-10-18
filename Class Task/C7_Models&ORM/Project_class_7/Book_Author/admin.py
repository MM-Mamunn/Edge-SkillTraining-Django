
from django.contrib import admin
from .models import Author, Book,Publisher_all

# Register Author model
admin.site.register(Author)

# Register Book model
admin.site.register(Book)
admin.site.register(Publisher_all)