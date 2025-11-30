from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        validate_password(attrs["password1"])
        return attrs

    def create(self, validated_data):
        # Extract passwords first
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        # Create user WITHOUT password
        user = User.objects.create(
            email=validated_data["email"],
        )

        # Hash password
        user.password = make_password(password)
        user.save()

        return user
