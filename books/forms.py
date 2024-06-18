from django import forms
from django.core.validators import ValidationError

from .models import Author, Book, Genre


class AddBookForm(forms.ModelForm):
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(), empty_label="Укажите жанр"
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), empty_label="Укажите автора"
    )

    class Meta:
        model = Book
        fields = (
            "title",
            "description",
            "slug",
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

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) > 70:
            raise ValidationError("Максимальная длина заголовка 70")

        return title


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Файл")
