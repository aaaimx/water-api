from __future__ import unicode_literals
from django.db import models
from uuid import uuid4
from .managers import UserManager

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from apps.states.models import State


class User(AbstractUser):

    user_state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email
