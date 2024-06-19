from books.utils import menu


def get_book_context(requset):
    return {
        "mainmenu": menu,
    }
