from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from django.conf import settings

import datetime
from django.utils import timezone


class Clinic(models.Model):
    name = models.CharField(
        max_length=200, help_text=_("name of the clinic"), verbose_name=_("name")
    )
    rep = models.ForeignKey(
        CustomUser,
        null=True,
        help_text=_("representative of the clinic"),
        verbose_name=_("rep"),
        on_delete=models.SET_NULL,
        related_name="clinics",
    )
    address = models.CharField(
        help_text=_("address of the clinic"), verbose_name=_("address"), max_length=300
    )
    is_verified = models.BooleanField("verified by admin", default=False)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        help_text=_("the clinic that this time slot belongs to"),
        verbose_name=_("clinic"),
        on_delete=models.CASCADE,
        related_name="time_slots",
    )
    start_time = models.DateTimeField("start time", default=timezone.now, blank=True)
    end_time = models.DateTimeField(
        "end time", default=timezone.now() + datetime.timedelta(hours=3), blank=True
    )

    reserver = models.ForeignKey(
        CustomUser,
        help_text=_("reserver of the this timeslot"),
        verbose_name=_("reserver"),
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="reserved_slots",
    )

    def __str__(self):
        return f"{self.clinic.name} {self.start_time} until {self.end_time}"

