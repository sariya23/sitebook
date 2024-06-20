from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "password")


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirm",
        )
        labels = {
            "email": "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }

    username = UsernameField(label="Логин")
    password = forms.CharField(
        max_length=255, label="Пароль", widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput()
    )

    def clean_password_confirm(self):
        clean_data = self.cleaned_data

        if clean_data["password"] != clean_data["password_confirm"]:
            raise ValidationError("Пароль не совпадают")
        return clean_data["password"]

    def clean_email(self):
        email = self.cleaned_data["email"]

        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Такой email уже существует")
        return email
