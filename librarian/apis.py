from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import *
from .models import *
from rest_framework.generics import get_object_or_404


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BarrowBookApi(ViewSet):
    queryset = Barrow.objects.select_related('member', 'book').all()
    serializer_class = BarrowSerializer

    def create(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            instance = serialized_data.create()
            return Response(data=self.serializer_class(instance=instance).data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            _instance = get_object_or_404(self.queryset, id=pk)
            instance = serialized_data.update(instance=_instance, validated_data=serialized_data.validated_data)
            return Response(data=self.serializer_class(instance=instance), status=status.HTTP_202_ACCEPTED)

    def list(self, request):
        serialized_data = self.serializer_class(instance=self.queryset.filter(member=request.user), many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        serialized_data = self.serializer_class(instance=get_object_or_404(self.queryset, id=pk))
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        get_object_or_404(self.queryset, id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


