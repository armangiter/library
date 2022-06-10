from django.db import models

from accounts.models import Member
from core.models import BaseModel
from django.utils import timezone


class Book(BaseModel):
    name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, verbose_name='ISBN', help_text='International Standard Book Number')
    author = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.PositiveSmallIntegerField(default=0)

    def subtract_inventory(self, amount=1):
        self.inventory -= amount
        if self.inventory >= 0:
            self.save()
            return True
        return False


class Barrow(BaseModel):
    book = models.ForeignKey(to=Book, on_delete=models.PROTECT, related_name='Barrows')
    member = models.ForeignKey(to=Member, on_delete=models.PROTECT, related_name='Barrows')
    barrow_date = models.DateTimeField(default=timezone.now)
    barrow_time = models.DurationField()
    return_date = models.DateTimeField()
