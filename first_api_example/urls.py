from django.urls import path

from first_api_example import views

urlpatterns = [
    path("my_api/", views.MyAPIView.as_view()),
]
