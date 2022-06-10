from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier
