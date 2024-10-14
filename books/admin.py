from django.contrib import admin

from books import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    ...
