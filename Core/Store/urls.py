
from django.urls import path
from . import views


urlpatterns = [
    path("products/",views.AllProducts,name="All Products")
]