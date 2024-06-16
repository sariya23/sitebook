from django.contrib import admin

from .models import Author, Book, Genre, Tags

# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Tags)
admin.site.register(Author)
