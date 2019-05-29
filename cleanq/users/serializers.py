from .models import CustomUser
from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password", "is_basic", "is_rep")

    def create(self, validated_data):

        user = UserModel.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.is_rep = False
        user.is_basic = True
        user.save()

        return user
