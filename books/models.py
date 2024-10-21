from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Book(models.Model):
    class TypeChoices(models.TextChoices):
        HARDCOVER = "HC", "Твёрдый переплёт"
        PAPERCOVER = "PB", "Мягкий переплёт"
        EBOOK = "EB", "Электроная книга"

    title = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(default="")
    book_type = models.CharField(
        max_length=2,
        choices=TypeChoices.choices,
        default=TypeChoices.PAPERCOVER,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    rating = models.FloatField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books",
    )
    tags = models.ManyToManyField(
        "books.Tag",
        blank=True,
        related_name="books",
    )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name

