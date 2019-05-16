from .models import ClinicRepresentative, 
from rest_framework import serializers


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("url", "username", "email")
