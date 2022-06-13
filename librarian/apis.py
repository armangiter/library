from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


BARROW_ACTION_PARAMETERS = [
    openapi.Parameter('book', openapi.IN_BODY, description="the book id", type=openapi.TYPE_INTEGER, required=True),
    openapi.Parameter('member', openapi.IN_BODY, description='the member id', type=openapi.TYPE_INTEGER, required=True),
    openapi.Parameter('action_date', openapi.IN_BODY, description='this filed is', type=openapi.TYPE_STRING),
    openapi.Parameter('member', openapi.IN_BODY, description='the member id', type=openapi.TYPE_INTEGER),
    openapi.Parameter('member', openapi.IN_BODY, description='the member id', type=openapi.TYPE_INTEGER),
]


class BarrowBookApi(APIView):
    serializer_class = BarrowActionSerializer

    @swagger_auto_schema(method='post',
                         operation_description="""
                         action_types:
                            barrow_book = 1
                            return_book = 2
                            holdover_book = 3
                            
                            not:
                            for barrow and holdover "barrow_days" must be initialed in request body, its 0 by default 
                         """,
                         request_body=serializer_class,
                         responses={200: serializer_class(),
                                    204: 'this book is not available in the library',
                                    400: 'book or member or action_type does not exist'})
    @action(detail=True, methods=['post'], parser_classes=(MultiPartParser,))
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            instance = serialized_data.create(validated_data=serialized_data.validated_data)
            if isinstance(instance, BarrowAction):
                return Response(data=self.serializer_class(instance=instance).data, status=status.HTTP_201_CREATED)
            return Response(data={'error': instance}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(responses={200: serializer_class(read_only=True)})
    def get(self, request):
        serialized_data = self.serializer_class(instance=BarrowAction.objects.all(), many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)
