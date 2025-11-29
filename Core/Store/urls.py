
from django.urls import path
from . import views


urlpatterns = [
    path("products/",views.Products,name="Products"),
    path("category/",views.Category,name="Products Category"),
    path("allproducts/",views.AllProducts,name="All Products "),
]