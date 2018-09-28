from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.custom_auth.enums import RoleTypes


class User(AbstractUser):
    role = models.CharField(max_length=24,
                            choices=RoleTypes.Choices,
                            default=RoleTypes.COMMON)

# Create your models here.
