from django.contrib import admin
from .models import Member
from librarian.admin import BarrowActionInline


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = ('password', 'is_staff', 'role', 'username', 'email', 'is_active', 'is_superuser')
    list_display = ('username', 'role', 'is_active', 'is_superuser')
    list_editable = ('is_active', )
    inlines = (BarrowActionInline, )
