from django import template
from django.db.models import Count

from ..models import Genre, Tags

register = template.Library()


@register.inclusion_tag("books/list_genres.html")
def show_genres(genre_selected=0) -> dict[str, list[dict]]:
    genres = Genre.objects.annotate(total=Count("books")).filter(total__gt=0)
    return {"genres": genres, "genre_selected": genre_selected}


@register.inclusion_tag("books/list_tags.html")
def show_tags():
    return {"tags": Tags.objects.annotate(total=Count("tags")).filter(total__gt=0)}
