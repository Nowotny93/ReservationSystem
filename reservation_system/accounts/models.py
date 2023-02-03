from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from reservation_system.accounts.managers import ReservationSystemUserManager


class ReservationSystemUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=15,
        unique=True,
        null=True
    )
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(auto_now_add=True, )

    USERNAME_FIELD = 'email'

    objects = ReservationSystemUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        ReservationSystemUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *