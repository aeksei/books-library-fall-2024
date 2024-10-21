from django.shortcuts import render

from rest_framework.views import APIView  # Вместо from django.views import View
from rest_framework.request import Request
from rest_framework.response import Response  # Вместо from django.http import JsonResponse
from rest_framework import status  # Статус коды HTTP ответов


class MyAPIView(APIView):
    """
    Класс представления для обработки API запросов.
    """

    # Обработчик GET запроса.
    def get(self, request: Request) -> Response:
        data = {  # Ответ с информацией о методе запроса и переданных параметрах
            'method': request.method,
            'query_params': request.query_params,  # Получаем параметры запроса
        }
        return Response(data=data)

    # Обработчик POST запроса.
    def post(self, request: Request) -> Response:
        return Response({  # Ответ с информацией о методе запроса и теле запроса.
            "method": request.method,
            "data": request.data  # Получаем тело запроса
        })

    # Обработчик PUT запроса
    def put(self, request: Request) -> Response:
        return Response({  # Ответ с информацией о методе запроса и теле запроса.
            "method": request.method,
            "data": request.data  # Получаем тело запроса
        })

    # Обработчик PATCH запроса
    def patch(self, request: Request) -> Response:
        return Response({  # Ответ с информацией о методе запроса и теле запроса.
            "method": request.method,
            "data": request.data  # Получаем тело запроса
        })

    # Обработчик DELETE запроса
    def delete(self, request: Request) -> Response:
        return Response(  # Метод DELETE не возвращает тело запроса
            status=status.HTTP_204_NO_CONTENT
        )
