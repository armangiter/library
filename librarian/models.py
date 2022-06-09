from django.db import models
from core.models import BaseModel
from django.utils import timezone


class Book(BaseModel):
    name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, verbose_name='ISBN', help_text='International Standard Book Number')
    inventory = models.IntegerField(default=0)


class Barrow(BaseModel):
    barrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField()
