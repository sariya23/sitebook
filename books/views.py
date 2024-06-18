from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView, ListView

from .forms import AddBookForm, UploadFileForm
from .models import Book, Tags, UploadFile

menu = [
    {"title": "Home", "url_name": "home"},
    {"title": "About", "url_name": "about"},
    {"title": "Add book", "url_name": "add_book"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"},
]


class BookHome(ListView):
    template_name = "books/index.html"
    context_object_name = "books"
    extra_context = {
        "title": "Home page",
        "menu": menu,
        "genre_selected": 0,
    }

    def get_queryset(self):
        return Book.published_book.all().select_related("genre")


class AddBook(FormView):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = AddBookForm(request.POST)

        data = {
            "menu": menu,
            "title": "Добавить книгу",
            "form": form,
        }
        return render(request, "books/add_book.html", data)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("home")
        data = {
            "menu": menu,
            "title": "Добавить книгу",
            "form": form,
        }
        return render(request, "books/add_book.html", data)


class BookGenres(ListView):
    template_name = "books/index.html"
    context_object_name = "books"
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(
            genre__slug=self.kwargs["genre_slug"]
        ).select_related("genre")

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        genre = context["books"][0].genre
        context["title"] = genre.genre
        context["menu"] = menu
        context["genre_selected"] = genre.pk
        return context


class BookTags(ListView):
    template_name = "books/index.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.published_book.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("genre")

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tags.objects.get(slug=self.kwargs["tag_slug"])
        context["title"] = tag.tag
        context["menu"] = menu
        context["slug_selected"] = None
        return context


class ShowBook(DetailView):
    template_name = "books/book.html"
    slug_url_kwarg = "book_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["book"].title
        context["menu"] = menu
        return context

    def get_object(self, queryset=...):
        return get_object_or_404(
            Book.published_book, slug=self.kwargs[self.slug_url_kwarg]
        )


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Contact with us page")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Login page")


def page_not_found(request: HttpRequest, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Page not found</h1>")


def about(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = UploadFile(file=form.cleaned_data["file"])
            upload_file.save()
    else:
        form = UploadFileForm()
    return render(
        request, "books/about.html", {"title": "About page", "menu": menu, "form": form}
    )
