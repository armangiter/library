from django.urls import path
from . import apis


app_name = 'library'

urlpatterns = [
    path('book-list/', apis.BookListView.as_view(), name='book_list'),
    path('barrow/<int:pk>', apis.BarrowBookApi.as_view(), name='barrow_book')
]

