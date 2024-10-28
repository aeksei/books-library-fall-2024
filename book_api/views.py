from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404

from books.models import Book
from book_api.serializers import BookSerializer


class ListCreateBookAPIView(APIView):
    """По /books/ получаем список объектов или доабвляем новый."""
    def get(self, request: Request, *args, **kwargs):
        """Список книг"""
        queryset = (
            Book.objects.all()
            .prefetch_related("tags")
            .select_related("category")
        )

        serializer = BookSerializer(
            instance=queryset,
            many=True,
        )

        return Response(data=serializer.data)

    def post(self, request: Request, *args, **kwargs):
        """Добавление книги"""
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class RetrieveUpdateDeleteBookAPIView(APIView):
    """

    По /books/<int:pk>/
    - получаем детальное представление объекта - GET
    - обновление через PUT/PATCH
    - удаление DELETE
    """
    def get(self, request: Request, *args, **kwargs):
        instance = get_object_or_404(Book, **kwargs)  # get_object_or_404(Book,**kwargs pk=pk)

        serializer = BookSerializer(instance=instance)

        return Response(data=serializer.data)

    def put(self, request: Request, *args, **kwargs):
        instance = get_object_or_404(Book, **kwargs)

        serializer = BookSerializer(
            instance=instance,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request: Request, *args, **kwargs):
        instance = get_object_or_404(Book, **kwargs)

        serializer = BookSerializer(
            instance=instance,
            data=request.data,
            partial=True,  # Частичное обновление
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request: Request, *args, **kwargs):
        instance = get_object_or_404(Book, **kwargs)

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
