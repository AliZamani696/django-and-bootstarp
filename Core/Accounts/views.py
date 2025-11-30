from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework.response import Response



class RegisterView(APIView):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return render(request, "login.html", {
                "success": "Account created successfully!"
            })

        return Response({
            "errors": serializer.errors
        })
