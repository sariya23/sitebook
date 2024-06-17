from django import forms

from .models import Author, Genre


class AddBookForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"required": True}),
        required=False,
        label="Заголовок",
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"required": True, "cols": 50, "rows": 5}),
        required=False,
        label="Описание",
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
