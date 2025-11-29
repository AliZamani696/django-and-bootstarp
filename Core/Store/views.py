from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def AllProducts(req):
    return HttpResponse("<h1>Products page</h1>")
