app_name ="accounts"
from django.urls import path
from .views import (
    # LoginView,
    # LoginAPIView,
    # RegistrationApiView
    # SignupView
    RegisterView
)

urlpatterns = [
    # path("api/loginView/",LoginView.as_view()),
    path("api/register/",RegisterView.as_view()),
    # path("api/login/",LoginAPIView.as_view()),
    # path("login/",SignupView.as_view())
]