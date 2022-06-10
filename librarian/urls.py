from django.urls import path
from . import apis


app_name = 'library'

urlpatterns = [
    path('book-list/', apis.BookListView.as_view(), name='book_list'),
]
