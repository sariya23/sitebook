from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Author, Book, Genre, Tags


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "slug",
        "author",
        "description",
        "rating",
        "genre",
        "tags",
        "is_published",
    )
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("id", "title", "time_create", "rating", "genre", "is_published")
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_per_page = 5
    actions = ("set_published", "set_draft")
    search_fields = ("title",)
    list_filter = ("genre",)
    filter_horizontal = ("tags",)

    @admin.action(description="Опубликовать выбранное")
    def set_published(self, request: HttpRequest, quesryset: QuerySet):
        count = quesryset.update(is_published=1)
        self.message_user(request, f"Опубликовано {count} записей(сь)")

    @admin.action(description="Снять с публикации")
    def set_draft(self, request: HttpRequest, quesryset: QuerySet):
        count = quesryset.update(is_published=0)
        self.message_user(
            request, f"Снято с публикации {count} записей(сь)", messages.WARNING
        )


@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("genre",)}
    list_display = ("id", "genre")
    list_display_links = ("id", "genre")
    ordering = ("id",)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}
    list_display = ("id", "tag")
    list_display_links = ("id", "tag")
    ordering = ("id",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "surname")}
    list_display = ("id", "name", "surname")
    list_display_links = ("id", "name", "surname")
    ordering = ("id",)
