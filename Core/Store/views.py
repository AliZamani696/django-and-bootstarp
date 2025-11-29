from django.shortcuts import render
from .models import Product,Category 
# Create your views here.


def Products(req):
    Products = Product.objects.all()
    return render(req,"index.html",{"products":Products})
def category(req):
    return render(req,"category.html")
def AllProducts(req):
    Products = Product.objects.all()
    category = Category.objects.all()
    return render(req,"allproducts.html",{"products":Products,"category":category})

def About(req):
    return render(req,"about.html")

def Contact(req):
    return render(req,"contact.html")
def Cart(req):
    return render(req,"cart.html")
def LoginAndSignin(req):
    return render(req,"login.html")