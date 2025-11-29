from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.


def Products(req):
    return render(req,"index.html")
def Category(req):
    return render(req,"category.html")
def AllProducts(req):
    return render(req,"allproducts.html")