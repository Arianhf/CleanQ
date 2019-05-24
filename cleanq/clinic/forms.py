from django import forms
from clinic.models import TimeSlot, Clinic


class TimeslotCreateForm(forms.ModelForm):
    clinic = forms.ModelChoiceField(
        label="", queryset=Clinic.objects.all(), empty_label="Select Clinic"
    )

    def __init__(self, *args, **kwargs):
        rep = kwargs.pop("user", None)
        super(TimeslotCreateForm, self).__init__(*args, **kwargs)
        if rep is not None:
            self.fields["clinic"].queryset = Clinic.objects.filter(rep=rep)

    class Meta:
        model = TimeSlot
        fields = ["start_time", "end_time", "clinic"]
        widgets = {
            "start_date": forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"]),
            "end_date": forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"]),
        }
