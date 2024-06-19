from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginUserForm


def login_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(
                request,
                username=credentials["username"],
                password=credentials["password"],
            )
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginUserForm()
    return render(request, "users/login.html", {"form": form})


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse("users:login_user"))
