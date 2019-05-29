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
from clinic.forms import (
    TimeslotCreateForm,
    TimeslotReserveForm,
    TimeslotClinicReserveForm,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import rep_required, basic_required
from django.utils import timezone
from django.contrib import messages


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
        and Optionally restricts the returned slots to a given clinic,
        by filtering against a `clinic_name` query parameter in the URL.
        """
        queryset = TimeSlot.objects.filter(reserver=None)
        clinic_name = self.request.query_params.get("clinic_name", None)
        if clinic_name is not None:
            queryset = queryset.filter(clinic__name__contains=clinic_name)
        return queryset


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
    template_name = "clinic/timeslot_list_user.html"

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


@method_decorator(rep_required, name="dispatch")
@method_decorator(login_required, name="dispatch")
class ClinicReservedTimeSlotsList(generic.ListView):
    """Generic class-based list view for a list of clinics."""

    model = TimeSlot
    ordering = "start_time"
    paginate_by = 15

    def get_queryset(self):
        user = self.request.user
        return TimeSlot.objects.filter(pk=self.kwargs.get("pk"))


@method_decorator(rep_required, name="dispatch")
@method_decorator(login_required, name="dispatch")
class ClinicPastReservedTimeSlotsList(generic.ListView):
    """Generic class-based list view for a list of clinics."""

    model = TimeSlot
    ordering = "start_time"
    paginate_by = 15

    def get_queryset(self):
        user = self.request.user

        now = timezone.now()

        return TimeSlot.objects.filter(pk=self.kwargs.get("pk"), end_time__lt=(now))


@basic_required
@login_required
def reserve_slot(request):
    if request.method == "POST":
        form = TimeslotReserveForm(request.POST)
        timeslot = TimeSlot.objects.get(pk=request.POST.get("timeslot"))
        timeslot.reserver = request.user
        timeslot.save()

        messages.success(request, "reserved succesfully.")
        form = TimeslotReserveForm()
        return render(request, "clinic/reserve.html", {"form": form})
    else:
        form = TimeslotReserveForm()
    return render(request, "clinic/reserve.html", {"form": form})


@basic_required
@login_required
def reserve_slot_clinic(request, pk):
    if request.method == "POST":
        form = TimeslotClinicReserveForm(request.POST)
        form.fields["timeslot"].queryset = TimeSlot.objects.filter(
            reserver=None, clinic__is_verified=True, clinic=Clinic.objects.get(pk=pk)
        )
        print(
            TimeSlot.objects.filter(
                reserver=None,
                clinic__is_verified=True,
                clinic=Clinic.objects.get(pk=pk),
            )
        )
        timeslot = TimeSlot.objects.get(pk=request.POST.get("timeslot"))
        timeslot.reserver = request.user
        timeslot.save()

        messages.success(request, "reserved succesfully.")
        form = TimeslotClinicReserveForm()
        form.fields["timeslot"].queryset = TimeSlot.objects.filter(
            reserver=None, clinic__is_verified=True, clinic=Clinic.objects.get(pk=pk)
        )
        return render(request, "clinic/reserve.html", {"form": form})
    else:
        form = TimeslotClinicReserveForm()
        form.fields["timeslot"].queryset = TimeSlot.objects.filter(
            reserver=None, clinic__is_verified=True, clinic=Clinic.objects.get(pk=pk)
        )
    return render(request, "clinic/reserve.html", {"form": form})

