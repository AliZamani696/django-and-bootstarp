from django.shortcuts import render
from .models import Product
# Create your views here.


def Products(req):
    Products = Product.objects.all()
    return render(req,"index.html",{"products":Products})
def Category(req):
    return render(req,"category.html")
def AllProducts(req):
    return render(req,"allproducts.html")