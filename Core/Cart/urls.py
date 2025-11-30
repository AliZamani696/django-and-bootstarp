from django.urls import path
from .views import *

urlpatterns = [
    path("add/", AddToCartAPIView.as_view()),
    # path("item/<int:item_id>/remove/", RemoveFromCartAPIView.as_view()),
    # path("item/<int:item_id>/update/", UpdateQuantityAPIView.as_view()),
    # path("", GetCartAPIView.as_view()),
]
