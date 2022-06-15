from django.db import models
from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce
from rest_framework.generics import get_object_or_404

from accounts.models import Member
from core.models import BaseModel
from django.utils import timezone


class Book(BaseModel):
    name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, verbose_name='ISBN', help_text='International Standard Book Number')
    author = models.ForeignKey(to='Author', on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.SET_NULL, null=True, blank=True)

    @classmethod
    def get_books_inventory_balance(cls):
        barrow_count = Count('actions__id',
                             filter=Q(actions__action_type=1)
                             )
        return_count = Count('actions__id',
                             filter=Q(actions__action_type=2))
        books = Book.objects.all().annotate(
            in_use=Coalesce(barrow_count, 0) - Coalesce(return_count, 0)
        )
        return books

    @classmethod
    def get_book_balance(cls, book):
        barrow_count = Count('id',
                             filter=Q(action_type=1)
                             )
        return_count = Count('id',
                             filter=Q(action_type=2))
        book_balance = book.actions.all().aggregate(
            barrows=Coalesce(barrow_count, 0),
            returns=Coalesce(return_count, 0)
        )
        return book_balance

    def __str__(self):
        return f'{self.name} {self.author}, {self.publisher}'


class BarrowAction(BaseModel):
    BARROW = 1
    RETURN = 2
    HOLDOVER = 3

    book = models.ForeignKey(to=Book, on_delete=models.PROTECT, related_name='actions')
    member = models.ForeignKey(to=Member, on_delete=models.PROTECT, related_name='actions')
    action_type = models.SmallIntegerField(
        choices=((BARROW, 'barrow book'), (RETURN, 'return book'), (HOLDOVER, 'holdover book')))
    action_date = models.DateTimeField(default=timezone.now)
    barrow_days = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.book} >> {self.member}'

    @classmethod
    def barrow_book(cls, **kwargs):
        book = kwargs['book']
        book_balance = Book.get_book_balance(book)
        if book_balance['barrows'] == book_balance['returns']:
            instance = cls.objects.create(**kwargs, action_type=cls.BARROW)
            return instance
        return 'book is not available'

    @classmethod
    def holdover_book(cls, **kwargs):
        instance = cls.objects.create(**kwargs, action_type=cls.HOLDOVER)
        return instance

    @classmethod
    def return_book(cls, **kwargs):
        instance = cls.objects.create(**kwargs, action_type=cls.RETURN)
        return instance

    @staticmethod
    def action_switcher(action):
        if action == 1:
            return BarrowAction.barrow_book
        if action == 2:
            return BarrowAction.return_book
        if action == 3:
            return BarrowAction.holdover_book


class Author(BaseModel):
    first_name = models.CharField(max_length=50, default='author')
    last_name = models.CharField(max_length=50, default='author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'
