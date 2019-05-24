from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from django.utils.translation import gettext_lazy as _

from rest_framework import generics

from users import models
from users import serializers
from django.http import HttpResponseRedirect

from django.contrib.auth.views import auth_login


class SignUpView(TemplateView):
    template_name = "registration/signup.html"


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer

