from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from django.conf import settings
from django.shortcuts import reverse

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

    def get_absolute_url(self):
        """Returns the url to access a detail record for this clinic."""
        return reverse("clinic-detail", args=[str(self.id)])

    class meta:
        ordering = ["name"]
        verbose_name = _("clinic")
        verbose_name_plural = _("clinics")


class TimeSlot(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        help_text=_("the clinic that this time slot belongs to"),
        verbose_name=_("clinic"),
        on_delete=models.CASCADE,
        related_name="time_slots",
    )
    start_time = models.DateTimeField("start time", default=None, blank=True)
    end_time = models.DateTimeField("end time", default=None, blank=True)

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

    class meta:
        ordering = ["clinic"]
        verbose_name = _("timeslot")
        verbose_name_plural = _("timeslots")
