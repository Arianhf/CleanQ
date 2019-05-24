from django import forms
from django.forms import ValidationError

from clinic.models import TimeSlot, Clinic
import datetime
from django.utils import timezone


class TimeslotCreateForm(forms.ModelForm):
    clinic = forms.ModelChoiceField(
        label="", queryset=Clinic.objects.all(), empty_label="Select Clinic"
    )

    def __init__(self, *args, **kwargs):
        rep = kwargs.pop("user", None)
        super(TimeslotCreateForm, self).__init__(*args, **kwargs)
        if rep is not None:
            self.fields["clinic"].queryset = Clinic.objects.filter(rep=rep)

    def clean_start_time(self):
        start_time = self.cleaned_data["start_time"]

        if start_time < timezone.now():
            raise ValidationError("start time should be in the future")
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data["end_time"]

        if end_time < timezone.now():
            raise ValidationError("end time should be in the future")

        return end_time

    def clean(self):
        end_time = self.cleaned_data["end_time"]
        start_time = self.cleaned_data["start_time"]

        if start_time > end_time:
            raise ValidationError("end time can't be before start time")

        if end_time - start_time < timezone.timedelta(hours=1):
            raise ValidationError(
                "gap between start and end should be greater that 1 hour"
            )

    class Meta:
        model = TimeSlot
        fields = ["start_time", "end_time", "clinic"]
        widgets = {
            "start_date": forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M"]),
            "end_date": forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M"]),
        }


class TimeslotReserveForm(forms.Form):
    timeslot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.filter(reserver=None, clinic__is_verified=True)
    )
