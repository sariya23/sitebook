from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("profile/", views.UserProfile.as_view(), name="profile"),
]
