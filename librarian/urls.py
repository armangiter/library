from django.urls import path
from . import apis


urlpatterns = [
    path('book-list/', apis.BookListView.as_view(), name='book_list'),
]
