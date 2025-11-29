
from django.urls import path
from . import views


urlpatterns = [
    path("products/",views.Products,name="Products"),
    path("category/",views.category,name="Products Category"),
    path("allproducts/",views.AllProducts,name="All Products "),
    path("about/",views.About,name="About"),
    path("contact/",views.Contact,name="Contact"),
    path("cart/",views.Cart,name="Cart"),
    path("login/",views.LoginAndSignin,name="LoginAndSignin"),
]