from typing import Any, Optional

menu = [
    {"title": "Home", "url_name": "home"},
    {"title": "About", "url_name": "about"},
    {"title": "Add book", "url_name": "add_book"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"},
]


class DataMixin:
    title_page: Optional[str] = None
    genre_selected: Optional[int] = None
    extra_context: dict[str, Any] = {}

    def __init__(self):
        if self.title_page is not None:
            self.extra_context["title"] = self.title_page

        if "menu" not in self.extra_context:
            self.extra_context["menu"] = menu

        if self.genre_selected is not None:
            self.extra_context["genre_selected"] = self.genre_selected

    def get_mixin_context(self, context: dict[str, Any], **kwargs):
        context["menu"] = menu
        context["genre_select"] = None
        context.update(kwargs)
        return context
