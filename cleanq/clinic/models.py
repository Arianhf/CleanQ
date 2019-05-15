from django.db import models
from users.models import ClinicRepresentative, BasicUser

import datetime
from django.utils import timezone

# settings.AUTH_USER_MODEL


class Clinic(models.Model):
    rep = models.ForeignKey(
        ClinicRepresentative,
        help_text=_("representative of the clinic"),
        verbose_name=_("rep"),
        on_delete=models.SET_NULL,
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
        "end time", default=timezone.now + datetime.timedelta(hours=3), blank=True
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

