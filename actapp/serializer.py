from rest_framework import serializers
from django.contrib.auth import  get_user_model
from .models import User 

class UserSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = User
        fields = ['email','password','is_verified']


class VerifyAccountSerializer(serializers.Serializer):
      email = serializers.EmailField()
      otp = serializers.CharField()
        