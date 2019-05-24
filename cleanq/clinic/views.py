from django.shortcuts import render

from clinic.models import Clinic, TimeSlot  # BasicUser, ClinicRepresentative
from clinic.serializers import (
    # BasicUserSerializer,
    # ClinicRepresentativeSerializer,
    ClinicSerializer,
    TimeSlotSerializer,
)
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.views import generic
from clinic.forms import TimeslotCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import rep_required, basic_required
from django.utils import timezone


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            # "basic-users": reverse("basicuser-list", request=request, format=format),
            # "representatives": reverse(
            #     "clinicrepresentative-list", request=request, format=format
            # ),
            "timeslots": reverse("timeslot-list", request=request, format=format),
            "clinics": reverse("clinic-list", request=request, format=format),
            "available-timeslots": reverse(
                "available-timeslots-list", request=request, format=format
            ),
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


# class ClinicRepresentativeList(generics.ListCreateAPIView):
#     queryset = ClinicRepresentative.objects.all()
#     serializer_class = ClinicRepresentativeSerializer


# class ClinicRepresentativeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ClinicRepresentative.objects.all()
#     serializer_class = ClinicRepresentativeSerializer


# class BasicUserList(generics.ListCreateAPIView):
#     queryset = BasicUser.objects.all()
#     serializer_class = BasicUserSerializer


# class BasicUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BasicUser.objects.all()
#     serializer_class = BasicUserSerializer


class availableTimeSlotsList(generics.ListAPIView):
    serializer_class = TimeSlotSerializer

    def get_queryset(self):
        """
        this view should return a list of all available
        timeslots for all clinics
        """
        return TimeSlot.objects.filter(reserver=None)


def index(request):
    clinics = Clinic.objects.all()

    context = {"clinics": clinics}

    return render(request, "clinic/index.html", context=context)


class ClinicDetailView(generic.DetailView):
    model = Clinic


@method_decorator(rep_required, name="dispatch")
@method_decorator(login_required, name="dispatch")
class TimeslotCreateView(generic.CreateView):
    model = TimeSlot
    form_class = TimeslotCreateForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(TimeslotCreateView, self).get_form_kwargs()
        if self.request.method == "GET":
            kwargs.update({"user": self.request.user})
        return kwargs


class ClinicListView(generic.ListView):
    """Generic class-based list view for a list of clinics."""

    model = Clinic
    ordering = "name"
    paginate_by = 15
    queryset = Clinic.objects.prefetch_related("time_slots")


@method_decorator(basic_required, name="dispatch")
@method_decorator(login_required, name="dispatch")
class UserReservedTimeSlotsList(generic.ListView):
    """Generic class-based list view for a list of clinics."""

    model = TimeSlot
    ordering = "start_time"
    paginate_by = 15

    def get_queryset(self):
        user = self.request.user
        return TimeSlot.objects.filter(reserver=user)


@method_decorator(basic_required, name="dispatch")
@method_decorator(login_required, name="dispatch")
class UserPastReservedTimeSlotsList(generic.ListView):
    """Generic class-based list view for a list of clinics."""

    model = TimeSlot
    ordering = "start_time"
    paginate_by = 15

    def get_queryset(self):
        user = self.request.user

        now = timezone.now()

        return TimeSlot.objects.filter(reserver=user, end_time__lt=(now))
