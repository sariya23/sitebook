from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Book

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


def show_genre(request: HttpRequest, genre_id: int) -> HttpResponse:
    context = {
        "title": "Home page",
        "menu": menu,
        "books": Book.published_book.all(),
        "genre_selected": genre_id,
    }
    return render(request, "books/index.html", context)


def page_now_found(request: HttpRequest, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page not found</h1>")
