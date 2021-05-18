from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = AccountManager()

    def __str__(self):
        return self.email
