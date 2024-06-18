from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("show_book/<slug:book_slug>/", views.show_book, name="book"),
    path("addbook/", views.add_book, name="add_book"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("genre/<slug:genre_slug>/", views.show_genre, name="genre"),
    path("tag/<slug:tag_slug>/", views.show_book_by_tag, name="tags"),
]
