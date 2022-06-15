from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book, BarrowAction


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'publisher', 'author')


class BarrowActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarrowAction
        fields = ('id', 'book', 'member', 'action_date', 'barrow_days', 'get_action_type_display', 'action_type')
        extra_kwargs = {
            'action_type': {'write_only': True},
            'get_action_type_display': {'read_only': True}
        }

    def validated_action_type(self):
        if self.initial_data['action_type'] in [1, 2, 3]:
            return self.initial_data['action_type']
        raise ValidationError('this field must be one of this {1, 2, 3}')

    def create(self, validated_data):
        _ = validated_data.pop('action_type')
        action = BarrowAction.action_switcher(_)
        instance = action(**validated_data)
        return instance
