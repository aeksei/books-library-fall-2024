# Generated by Django 4.2.11 on 2024-10-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_book_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(to="books.tag"),
        ),
    ]
