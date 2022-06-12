from django.db import models
from accounts.models import Member
from core.models import BaseModel
from django.utils import timezone


class Book(BaseModel):
    name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, verbose_name='ISBN', help_text='International Standard Book Number')
    author = models.ForeignKey(to='Author', on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.SET_NULL, null=True, blank=True)
    inventory = models.PositiveSmallIntegerField(default=0)

    def subtract_inventory(self, amount=1):
        self.inventory -= amount
        if self.inventory >= 0:
            self.save()
            return True
        return False

    def add_inventory(self, amount=1):
        self.inventory += amount
        self.save()


class Barrow(BaseModel):
    book = models.ForeignKey(to=Book, on_delete=models.PROTECT, related_name='Barrows')
    member = models.ForeignKey(to=Member, on_delete=models.PROTECT, related_name='Barrows')
    barrow_date = models.DateTimeField(default=timezone.now)
    barrow_time = models.DurationField(default=timezone.timedelta(days=7))
    return_date = models.DateTimeField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None
             ):
        if self.book.subtract_inventory():
            self.return_date = self.barrow_date + self.barrow_time
            super(Barrow, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Author(BaseModel):
    first_name = models.CharField(max_length=50, default='author')
    last_name = models.CharField(max_length=50, default='author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(BaseModel):
    name = models.CharField(max_length=150)
