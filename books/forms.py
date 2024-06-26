from django import forms
from django.core.validators import ValidationError

from .models import Author, Book, Genre


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "description",
            "slug",
            "photo",
            "author",
            "rating",
            "genre",
            "tags",
            "is_published",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "description": forms.Textarea(attrs={"cols": 50, "rows": 4}),
        }

    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(), empty_label="Укажите жанр", label="Жанр"
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label="Укажите автора",
        label="Автор",
    )

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) > 70:
            raise ValidationError("Максимальная длина заголовка 70")

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Файл")
