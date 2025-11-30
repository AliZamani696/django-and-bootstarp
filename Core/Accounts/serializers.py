from rest_framework import serializers
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from .models import User
from django.core import exceptions





class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=150,write_only=True)
    password2 = serializers.CharField(max_length=150,write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2"
        ]

    def validate(self,attrs):
        if attrs["password1"]  != attrs["password2"]:
            raise serializers.ValidationError({"message":"passwords doesn't match"})
        try:
            validate_password(attrs["password1"])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"email":list(e.messages)})
        return super().validate(attrs)
    
    def create(self,validated_data):
        '''
        this here we can use three method for set password for user registration
            1=> use a user password
            2=> use a make_password and delete user password because not declare password in user model
            3=> use User create_user and set password  
        '''
        # password = validated_data.pop("password1")
        validated_data.pop("password2")
        user = User.objects.create_user(
            email = validated_data["email"],
            password = validated_data["password1"]
        #  user,password = make_password(password)
        )
        # user,password = make_password(password)
        user.save()
        return user