from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Book, Genre, Tags

menu = [
    {"title": "Home", "url_name": "home"},
    {"title": "About", "url_name": "about"},
    {"title": "Add book", "url_name": "add_book"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"},
]


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home page",
        "menu": menu,
        "books": Book.published_book.all(),
        "genre_selected": 0,
    }
    return render(request, "books/index.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "books/about.html", {"title": "About page", "menu": menu})


def book(request: HttpRequest, book_slug: int) -> HttpResponse:
    book = get_object_or_404(Book, slug=book_slug)
    data = {
        "title": book.title,
        "menu": menu,
        "book": book,
        "genre_id": 1,
    }
    return render(request, "books/book.html", data)


def add_book(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Add book page")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Contact with us page")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Login page")


def show_genre(request: HttpRequest, genre_slug: str) -> HttpResponse:
    genre = get_object_or_404(Genre, slug=genre_slug)
    genres = Book.published_book.filter(genre_id=genre.pk)
    context = {
        "title": f"Жанр {genre.genre}",
        "menu": menu,
        "books": genres,
        "genre_selected": genre.pk,
    }
    return render(request, "books/index.html", context)


def show_book_by_tag(request: HttpRequest, tag_slug: str) -> HttpResponse:
    tag = get_object_or_404(Tags, slug=tag_slug)
    books_with_tag = tag.tags.filter(is_published=Book.PublishStatus.PUBLISHED)
    print(books_with_tag)
    data = {
        "title": tag.tag,
        "menu": menu,
        "books": books_with_tag,
        "slug_selected": None,
    }

    return render(request, "books/index.html", data)


def page_now_found(request: HttpRequest, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page not found</h1>")
