
from . import views
from django.urls import path
from .views import (
    HomeView,
    CategoryView,
    AllProductsView,
    AboutView,
    ContactView,
    CartView,
   
)



urlpatterns = [
    
    path("api/products/", HomeView.as_view()),
    path("api/categories/", CategoryView.as_view()),
    path("api/allproducts/",AllProductsView.as_view()),

    path("api/about/", AboutView.as_view()),
    path("api/contact/", ContactView.as_view()),
    path("api/cart/", CartView.as_view()),
]
