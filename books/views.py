from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import AddBookForm, UploadFileForm
from .models import Book, Tags, UploadFile
from .utils import DataMixin


class BookHome(DataMixin, ListView):
    template_name = "books/index.html"
    context_object_name = "books"
    title_page = "Home page"
    genre_selected = 0

    def get_queryset(self):
        return Book.published_book.all().select_related("genre")


class AddBook(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddBookForm
    template_name = "books/add_book.html"
    success_url = reverse_lazy("home")
    title_page = "Добавить книгу"
    permission_required = "books.add_book"

    def form_valid(self, form):
        book = form.save(commit=False)
        book.creator = self.request.user
        return super().form_valid(form)


class EditBookView(DataMixin, UpdateView):
    title_page = "Редактирование статьи"
    model = Book
    template_name = "books/add_book.html"
    fields = ["title", "description", "photo", "author", "genre", "tags"]


class BookGenres(DataMixin, ListView):
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
        return self.get_mixin_context(
            context, title=genre.genre, genre_selected=genre.pk
        )


class BookTags(DataMixin, ListView):
    template_name = "books/index.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.published_book.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("genre")

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tags.objects.get(slug=self.kwargs["tag_slug"])
        return self.get_mixin_context(context, title=tag.tag)


class ShowBook(DataMixin, DetailView):
    template_name = "books/book.html"
    slug_url_kwarg = "book_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context["book"].title)

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


@login_required
def about(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = UploadFile(file=form.cleaned_data["file"])
            upload_file.save()
    else:
        form = UploadFileForm()
    return render(request, "books/about.html", {"title": "About page", "form": form})
