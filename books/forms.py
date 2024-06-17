from django import forms
from django.core.validators import MinLengthValidator, ValidationError

from .models import Author, Genre


class AddBookForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"required": True}),
        required=False,
        label="Заголовок",
        min_length=5,
        error_messages={
            "min_length": "Слишком короткий заголовк",
            "required": "Обязательное поле",
        },
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"required": True, "cols": 50, "rows": 5}),
        required=False,
        label="Описание",
        validators=[
            MinLengthValidator(5, message="Минимальное число букв 5"),
        ],
    )
    is_published = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"required": True}),
        required=False,
        label="Опубликовано",
        initial=True,
    )
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=True,
        label="Жанр",
        empty_label="Выбирите жанр",
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=True,
        label="Автор",
        empty_label="Укажите атвора",
    )

    def clean__title(self):
        title = self.cleaned_data["title"]
        allowed_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ -0123456789"
        if not (set(title) < set(allowed_chars)):
            raise ValidationError(
                "Допусимы только русские символы, дефис, цифры и пробел"
            )
