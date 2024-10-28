from django.test import TestCase

from books.models import Book


class BookModelTestCase(TestCase):
    def test_str(self):
        expected_result = "test_title"
        obj = Book(title=expected_result)

        actual_result = str(obj)

        self.assertEqual(
            expected_result, actual_result,
            msg="Не работает строковое представление для книги."
        )
