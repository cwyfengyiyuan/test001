from . import models
from .utils import json_response
from rest_framework import status
from .serialiaers import AuthorModelSerializer, BookModelSerializer
from rest_framework.generics import GenericAPIView


# Create your views here.

class AuthorGenericAPIView(GenericAPIView):
    queryset = models.Author.objects
    serializer_class = AuthorModelSerializer

    authentication_classes = []

    def put(self, request):
        request_data = request.data
        name = request_data.get("name", "")
        obj = models.Author.objects.filter(name=name).first()
        return json_response(data=self.serializer_class(obj).data)

    def post(self, request):
        request_data = request.data
        author_check = AuthorModelSerializer(data=request_data)
        if author_check.is_valid():
            author_check.save()
            return json_response(data=author_check.data)
        else:
            return json_response(code=status.HTTP_400_BAD_REQUEST, msg=author_check.errors)


class BookGenericAPIView(GenericAPIView):
    queryset = models.Book.objects
    serializer_class = BookModelSerializer

    authentication_classes = []

    def put(self, request):
        request_data = request.data
        name = request_data.get("name", "")
        obj = models.Book.objects.filter(name=name).first()
        return json_response(data=self.serializer_class(obj).data)

    def post(self, request):
        request_data = request.data
        book_check = BookModelSerializer(data=request_data)
        if book_check.is_valid():
            book_check.save()
            return json_response(data=book_check.data)
        else:
            return json_response(code=status.HTTP_400_BAD_REQUEST, msg=book_check.errors)
