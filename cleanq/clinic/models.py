from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from django.conf import settings

import datetime
from django.utils import timezone


class ClinicRepresentative(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text=_("user of the representative"),
        verbose_name=_("user"),
        on_delete=models.CASCADE,
    )

    class Meta:
        permissions = [
            ("create_time_slot", "Can create new time slots for current clinic"),
            ("remove_time_slot", "Can remove time slots for current clinic"),
            ("remove_clinic", "Can remove a clinic"),
            ("create_clinic", "Can create new clinic"),
        ]


class BasicUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text=_("user of the basic user"),
        verbose_name=_("user"),
        on_delete=models.CASCADE,
    )


class Clinic(models.Model):
    rep = models.ForeignKey(
        ClinicRepresentative,
        null=True,
        help_text=_("representative of the clinic"),
        verbose_name=_("rep"),
        on_delete=models.SET_NULL,
    )
    address = models.CharField(
        help_text=_("representative of the clinic"),
        verbose_name=_("rep"),
        max_length=300,
    )


class TimeSlot(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        help_text=_("the clinic that this time slot belongs to"),
        verbose_name=_("clinic"),
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField("start time", default=timezone.now, blank=True)
    end_time = models.DateTimeField(
        "end time", default=timezone.now() + datetime.timedelta(hours=3), blank=True
    )

    reserver = models.ForeignKey(
        BasicUser,
        help_text=_("representative of the clinic"),
        verbose_name=_("rep"),
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
    )

