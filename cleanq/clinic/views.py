from django.shortcuts import render

from clinic.models import BasicUser, ClinicRepresentative, Clinic, TimeSlot
from clinic.serializers import (
    BasicUserSerializer,
    ClinicRepresentativeSerializer,
    ClinicSerializer,
    TimeSlotSerializer,
)
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "basic-users": reverse("basicuser-list", request=request, format=format),
            "representatives": reverse(
                "clinicrepresentative-list", request=request, format=format
            ),
            "timeslots": reverse("timeslot-list", request=request, format=format),
            "clinics": reverse("clinic-list", request=request, format=format),
        }
    )


class ClinicList(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ClinicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class TimeSlotList(generics.ListCreateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class TimeSlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class ClinicRepresentativeList(generics.ListCreateAPIView):
    queryset = ClinicRepresentative.objects.all()
    serializer_class = ClinicRepresentativeSerializer


class ClinicRepresentativeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClinicRepresentative.objects.all()
    serializer_class = ClinicRepresentativeSerializer


class BasicUserList(generics.ListCreateAPIView):
    queryset = BasicUser.objects.all()
    serializer_class = BasicUserSerializer


class BasicUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasicUser.objects.all()
    serializer_class = BasicUserSerializer

