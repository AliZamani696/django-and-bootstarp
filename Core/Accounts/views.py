from rest_framework.views import APIView
from django.shortcuts import redirect
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



#TODO:
# fix login bug[]


class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "registration/login.html"
    def get(self, request):
        return Response({})
    def post(self, request):
        action = request.data.get("action")
        if action == "register":
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": "Account created successfully!",
                })
            return Response({
                "errors": serializer.errors
            })
        elif action == "login":
                email = request.data.get("email")
                password = request.data.get("password")
                if not email and not password:
                    print(request.data)
                    return Response(
                        {"error": "username and password required"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                user = authenticate(email=email,password=password)
                if user is None:
                    return Response(
                        {"error": "Invalid credentials"},
                        status=status.HTTP_401_UNAUTHORIZED
                    )
                token, created = Token.objects.get_or_create(user=user)
                print(request.data)
                return Response({
                    "message": "Login successful",
                    "token": token.key,
                    "user": {
                    # "id": user.id,
                    "email": user.email.split("@")[0]
                    }}

                )