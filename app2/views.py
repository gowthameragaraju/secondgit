from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gowtham(request):
    return HttpResponse('<h1>im very bad boy</h1>')
def gmr(reuest):
    return HttpResponse('<h1>im very good boy</h1>')