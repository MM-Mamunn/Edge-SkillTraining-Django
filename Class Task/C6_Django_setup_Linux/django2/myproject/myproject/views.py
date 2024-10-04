# from django.http import HttpResponse
from django.shortcuts import render

def hello_django2(request):
    return render(request, 'mypage.html')

# def hello_django(request):
#     return HttpResponse("hello")