from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer



class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        print(password,username)

        if user is not None:
            login(request, user)  # creates session
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"
    def get(self, request):
        return Response()
    
