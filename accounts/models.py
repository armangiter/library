from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from django.db import models


class Member(AbstractUser):
    role = models.CharField(max_length=10, choices=(('staff', 'is staff'), ('member',  'is member')))
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'




