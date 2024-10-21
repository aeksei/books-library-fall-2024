from django.urls import path

from book_api import views

urlpatterns = [
    path(
        "books/",
        views.ListCreateBookAPIView.as_view(),
        name="book-list",
    ),
    path(
        "books/<int:pk>/",
        views.RetrieveUpdateDeleteBookAPIView.as_view(),
        name="book-detail",
    ),
]
