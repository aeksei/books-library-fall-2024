from django.db import models


class Book(models.Model):
    class BookTypeChoices(models.TextChoices):
        HARDCOVER = "HC", "Твёрдый переплёт"
        PAPERCOVER = "PB", "Мягкий переплёт"
        EBOOK = "EB", "Электроная книга"

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(default="")
    book_type = models.CharField(
        max_length=2,
        choices=BookTypeChoices.choices,
        default=BookTypeChoices.PAPERCOVER,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
