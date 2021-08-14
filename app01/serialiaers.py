from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publish_date', 'country', 'author_list']

        extra_kwargs = {
            'author': {'write_only': True},
            'author_list': {'read_only': True}
        }
