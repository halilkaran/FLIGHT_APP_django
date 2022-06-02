from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
    )
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        ]
        
        extra_kwargs = {
            "password" : {"write_only" : True},
            "password2" : {"write_only" : True},
        }



