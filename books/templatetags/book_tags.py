from django import template

from ..models import Genre, Tags

register = template.Library()


@register.inclusion_tag("books/list_genres.html")
def show_genres(genre_selected=0) -> dict[str, list[dict]]:
    genres = Genre.objects.all()
    return {"genres": genres, "genre_selected": genre_selected}


@register.inclusion_tag("books/list_tags.html")
def show_tags():
    return {"tags": Tags.objects.all()}
