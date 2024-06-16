from django.contrib import admin

from .models import Author, Book, Genre, Tags


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "rating", "is_published")
    list_display_links = ("id", "title")


@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = ("id", "genre")
    list_display_links = ("id", "genre")
    ordering = ("id",)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "tag")
    list_display_links = ("id", "tag")
    ordering = ("id",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname")
    list_display_links = ("id", "name", "surname")
    ordering = ("id",)
