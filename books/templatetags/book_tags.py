from django import template
from django.db.models import Count

from sitebook import settings

from ..models import Genre, Tags

register = template.Library()


@register.filter
def get_range(value):
    return range(value)


@register.inclusion_tag("books/list_genres.html")
def show_genres(genre_selected=0) -> dict[str, list[dict]]:
    genres = Genre.objects.annotate(total=Count("books")).filter(total__gt=0)
    return {"genres": genres, "genre_selected": genre_selected}


@register.inclusion_tag("books/list_tags.html")
def show_tags():
    return {"tags": Tags.objects.annotate(total=Count("tags")).filter(total__gt=0)}


@register.inclusion_tag("books/rating.html")
def show_rating(book_rating: int):
    return {"rating": book_rating, "star_path": settings.STAR_PATH}
