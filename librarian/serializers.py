from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import Book, BarrowAction
from django.db import transaction


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'inventory', 'publisher', 'author')


class BarrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarrowAction
        fields = ('id', 'book', 'member', 'barrow_date', 'barrow_days', 'return_date', 'barrow_type')

    def create(self, validated_data):
        with transaction.atomic():
            _book = validated_data['book']
            if _book.subtract_inventory():
                barrow = BarrowAction.objects.create(**validated_data)
        return barrow
