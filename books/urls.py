from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, type_name="year")


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("book/<slug:book_slug>/", views.book, name="book"),
    path("addbook/", views.add_book, name="add_book"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("genre/<slug:genre_slug>/", views.show_genre, name="genre"),
]
