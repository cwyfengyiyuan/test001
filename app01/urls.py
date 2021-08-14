from django.urls import path
from .views import AuthorGenericAPIView, BookGenericAPIView

urlpatterns = [
    path("author", AuthorGenericAPIView.as_view()),
    path("book", BookGenericAPIView.as_view()),
]