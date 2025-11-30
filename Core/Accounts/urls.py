from django.urls import path
from .views import (
    LoginView,
    LoginAPIView
    # SignupView
)

urlpatterns = [
    path("api/login/",LoginView.as_view()),
    path("api/login/",LoginAPIView.as_view()),
    # path("login/",SignupView.as_view())
]