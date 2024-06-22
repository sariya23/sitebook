from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookHome.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("show_book/<slug:book_slug>/", views.ShowBook.as_view(), name="book"),
    path("addbook/", views.AddBook.as_view(), name="add_book"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("genre/<slug:genre_slug>/", views.BookGenres.as_view(), name="genre"),
    path("tag/<slug:tag_slug>/", views.BookTags.as_view(), name="tags"),
    path("edit/<int:pk>/", views.EditBookView.as_view(), name="edit"),
]
