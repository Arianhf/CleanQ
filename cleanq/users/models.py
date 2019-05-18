from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_basic = models.BooleanField("basic status", default=True)
    is_rep = models.BooleanField("rep status", default=False)

    permissions = [
        ("create_time_slot", "Can create new time slots for current clinic"),
        ("remove_time_slot", "Can remove time slots for current clinic"),
        ("remove_clinic", "Can remove a clinic"),
        ("create_clinic", "Can create new clinic"),
        ("reserve_time_slot", "Can reserve time slots"),
    ]
