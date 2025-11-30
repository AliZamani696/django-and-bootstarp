from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer



class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"
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
