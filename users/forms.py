from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
    UsernameField,
)
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "password")


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        labels = {
            "email": "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-input"}),
            "first_name": forms.TextInput(attrs={"class": "form"}),
            "last_name": forms.TextInput(attrs={"class": "form"}),
        }

    username = UsernameField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        max_length=255, label="Пароль", widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]

        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Такой email уже существует")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
        labels = {
            "email": "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-input"}),
            "first_name": forms.TextInput(attrs={"class": "form"}),
            "last_name": forms.TextInput(attrs={"class": "form"}),
        }

    username = UsernameField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        disabled=True,
    )
    email = forms.CharField(
        label="E-mail",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        disabled=True,
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password1 = forms.CharField(
        label="Новый пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password2 = forms.CharField(
        label="Повторите новый пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
