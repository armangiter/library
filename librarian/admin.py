from django.contrib import admin
from .models import Book, Barrow
# Register your models here.

admin.site.register([Book, Barrow])
