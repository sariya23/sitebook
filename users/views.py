from django.http import HttpRequest, HttpResponse


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("login")


def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("logout")
