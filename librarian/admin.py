from django.contrib import admin
from .models import Book, BarrowAction, Author, Publisher


# Register your models here.


class BarrowActionInline(admin.TabularInline):
    model = BarrowAction
    fields = ('member', 'book', 'action_date', 'get_action_type_display', 'barrow_days')
    readonly_fields = ('member', 'book', 'action_date', 'get_action_type_display', 'barrow_days')
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publisher', 'is_active')
    list_editable = ('is_active',)
    fields = ('name', 'author', 'publisher', 'isbn')
    inlines = (BarrowActionInline,)


class BookInline(admin.TabularInline):
    model = Book
    fields = ('name', 'publisher', 'author')
    readonly_fields = ('name', 'publisher', 'author')
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    fields = ('first_name', 'last_name')
    inlines = (BookInline,)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
    inlines = (BookInline,)
