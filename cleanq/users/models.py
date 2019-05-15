from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass


class ClinicRepresentative(CustomUser):
    pass


class BasicUser(CustomUser):
    pass
