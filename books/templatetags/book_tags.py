from django import template

from ..views import genres

register = template.Library()

@register.simple_tag()
def get_genres() -> list[dict[str, str]]:
    return genres


@register.inclusion_tag("books/list_genres.html")
def show_genres(genre_selected=0) -> dict[str, list[dict]]:
    genres = get_genres()
    return {"genres": genres, "genre_selected": genre_selected}
    