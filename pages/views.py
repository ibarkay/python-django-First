from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user) 
    return HttpResponse("<h1>Hello World</h1>")


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2>Contact</h2>')


def about_view(request, *args, **kwargs):
    return HttpResponse('<h2>About page</h2>')


def social_view(request, *args, **kwargs):
    return HttpResponse('<h2>Social page</h2>')
