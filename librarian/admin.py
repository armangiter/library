from django.contrib import admin
from .models import Book, BarrowAction
# Register your models here.

admin.site.register([Book, BarrowAction])
