from django import template

from ..models import Genre

register = template.Library()


@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.inclusion_tag("books/list_genres.html")
def show_genres(genre_selected=0) -> dict[str, list[dict]]:
    genres = get_genres()
    return {"genres": genres, "genre_selected": genre_selected}
