from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
#to show the data to the anonmious user we import the product class from the model module
#This product class has bunch of useful method for getting data from our database


def index(request):
    products = Product.objects.all() #by using this method we get all the data from the database
    return render(request, 'index.html',
                  {'products': products})
#we pass dictionary as third argument and this dictionary contain the data to be pass to template


def new(request):
    return HttpResponse('New Page')
