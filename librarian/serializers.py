from rest_framework import serializers
from librarian.models import Book, Barrow


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'inventory', 'publisher', 'author')


class BarrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrow
        fields = ('id', 'book', 'member', 'barrow_date', 'barrow_time', 'return_date')
