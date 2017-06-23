from django.db import models
from django.db.models import Q
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime

# Create your models here.
class ManateeFoodUserManager(BaseUserManager):
    def _create_user(self, username, password, is_superuser, **extra_fields):
        """Create user with given username and password"""
        now = timezone.now()
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(username=username, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, is_superuser=False, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, is_superuser=True, **extra_fields)

class ManateeFoodUser(AbstractUser, PermissionsMixin):
    username = models.CharField(_("Username"), max_length=30, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50, blank=False)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=False)
    email = models.EmailField(_("Email"), max_length=255, blank=False)

    date_joined = models.DateTimeField(_("Registration Date"), auto_now_add=True)
    is_active = models.BooleanField(_("Active"), default=True, help_text=_("Defines whether user should be considered active or not. Use this instead of deleting an account."))

    objects = ManateeFoodUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return first_name + last_name

    def get_short_name(self):
        return username

    def __str__(self):
        return self.username
