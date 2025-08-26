from django.shortcuts import render
from django.http import request
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)