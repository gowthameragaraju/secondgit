from django.urls import path
from app2.views import *
app_name='somthing!'
urlpatterns=[
    path("gowtham/",gowtham,name='gowtham'),
    path('gmr/',gmr,name='gmr'),
]