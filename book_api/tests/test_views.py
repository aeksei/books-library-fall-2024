import unittest

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from books.models import Book, Category


class ListCreateBookAPIViewTestCase(APITestCase):
    def test_empty_list_books(self):
        url = reverse("book_api:book-list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        list_books = response.json()

        self.assertIsInstance(list_books, list)

        self.assertEqual(
            0, len(list_books),
            msg="Список книг должен быть пустым.")

    def test_list_books(self):
        url = reverse("book_api:book-list")
        expected_count_books = 10
        default_year = 2024
        Book.objects.bulk_create(
            [
                Book(
                    title=f"title_{i}",
                    year=default_year,
                    slug=f"slug_{i}"
                ) for i in range(expected_count_books)
            ]
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        list_books = response.json()

        self.assertIsInstance(list_books, list)

        self.assertEqual(
            expected_count_books, len(list_books),
            msg="Список книг должен быть пустым."
        )

    def test_create_book(self):
        url = reverse("book_api:book-list")

        category = Category.objects.create(name="test_category")
        data = {
            "title": "test_title",
            "slug": "test_slug",
            "year": 2024,
            "category": category.id,
        }

        response = self.client.post(url, data=data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        obj = response.json()
        self.assertIsInstance(obj, dict)


class RetrieveUpdateDeleteBookAPIViewTestCase(APITestCase):
    def test_retrieve_book(self):
        book = Book.objects.create(title="test_title", year=2024, slug=f"test_slug")

        url = reverse("book_api:book-detail", args=(book.pk,))  # kwargs = {"pk": book.pk}
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        obj = response.json()
        self.assertIsInstance(obj, dict)

    def test_retrieve_does_not_exist_book(self):
        does_not_exists_book_pk = 1000001
        url = reverse("book_api:book-detail", args=(does_not_exists_book_pk,))  # kwargs = {"pk": book.pk}
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_book(self):
        book = Book.objects.create(title="test_title", year=2024, slug=f"test_slug")

        url = reverse("book_api:book-detail", args=(book.pk,))  # kwargs = {"pk": book.pk}
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(0, Book.objects.count())

    def test_delete_does_not_exist_book(self):
        does_not_exists_book_pk = 1000001
        url = reverse("book_api:book-detail", args=(does_not_exists_book_pk,))  # kwargs = {"pk": book.pk}
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)