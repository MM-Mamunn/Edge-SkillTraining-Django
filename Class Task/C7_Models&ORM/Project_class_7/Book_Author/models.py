from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(default="2000-01-01")
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(default="2000-01-01")
    price = models.FloatField(default= 0.00)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
# class Publishers(models.Model):
#     name = models.CharField(max_length=200)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     address = models.CharField(max_length=2000,default="")

class Publisher_all(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    address = models.CharField(max_length=2000,default="")