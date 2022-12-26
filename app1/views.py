from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>this is my app1 first viwe</h1>')
def second(request):
    return HttpResponse('<h1>this is my app1 second viwe</h1>')