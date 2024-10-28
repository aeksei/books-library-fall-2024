from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from books.models import Book
from book_api.serializers import BookSerializer


class ListCreateBookAPIView(ListCreateAPIView):
    """По /books/ получаем список объектов или доабвляем новый."""
    queryset = Book.objects.all().prefetch_related("tags").select_related("category")
    serializer_class = BookSerializer


class RetrieveUpdateDeleteBookAPIView(RetrieveUpdateDestroyAPIView):
    """

    По /books/<int:pk>/
    - получаем детальное представление объекта - GET
    - обновление через PUT/PATCH
    - удаление DELETE
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
