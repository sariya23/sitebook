from typing import Any, Optional

from sitebook import settings

menu = [
    {"title": "Home", "url_name": "home"},
    {"title": "About", "url_name": "about"},
    {"title": "Add book", "url_name": "add_book"},
    {"title": "Contact", "url_name": "contact"},
]


class DataMixin:
    title_page: Optional[str] = None
    genre_selected: Optional[int] = None
    extra_context: dict[str, Any] = {}
    paginate_by = 3
    star_path = settings.STAR_PATH

    def __init__(self):
        if self.title_page is not None:
            self.extra_context["title"] = self.title_page
        self.extra_context["star_path"] = settings.STAR_PATH

        if "menu" not in self.extra_context:
            self.extra_context["menu"] = menu

        if self.genre_selected is not None:
            self.extra_context["genre_selected"] = self.genre_selected

    def get_mixin_context(self, context: dict[str, Any], **kwargs):
        context["menu"] = menu
        context["genre_selected"] = None
        context.update(kwargs)
        return context
