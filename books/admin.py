from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe

from .models import Author, Book, Genre, Tags


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "slug",
        "author",
        "photo",
        "book_photo",
        "description",
        "rating",
        "genre",
        "tags",
        "is_published",
    )
    list_display = (
        "id",
        "book_photo",
        "title",
        "time_create",
        "rating",
        "genre",
        "is_published",
    )
    save_on_top = True
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    readonly_fields = ("book_photo",)
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

    @admin.display(description="Обложка книги")
    def book_photo(self, book: Book):
        if book.photo:
            return mark_safe(f"<img src='{book.photo.url}' width=50>")
        return "Без обложки"


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
