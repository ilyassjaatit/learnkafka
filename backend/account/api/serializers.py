from rest_framework import serializers
from django.contrib.auth.models import User

from account.models import UserProfile


class RegistrationUserSerializer(serializers.ModelSerializer):
    """Registration Serializer"""
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    """User profile  Serializer"""

    class Meta:
        model = UserProfile
        fields = ['pk', 'user']
