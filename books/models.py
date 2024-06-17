from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models  # type: ignore
from django.urls import reverse  # type: ignore
from django.utils.text import slugify


class PublishedBookManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=1)


def translate_to_english(text: str) -> str:
    alphabet = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ы": "i",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    return slugify("".join(alphabet.get(w, w) for w in text.lower()))


class Book(models.Model):
    class Meta:
        ordering = ["id", "-rating", "-title"]
        indexes = [models.Index(fields=["-rating"])]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    genre = models.ForeignKey(
        "Genre", on_delete=models.PROTECT, related_name="books", verbose_name="Жанр"
    )
    tags = models.ManyToManyField(
        "Tags", blank=True, related_name="tags", verbose_name="Тэги"
    )
    title = models.CharField(max_length=70, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    author = models.ForeignKey(
        "Author",
        on_delete=models.SET_NULL,
        null=True,
        related_name="author",
        verbose_name="Автор",
    )
    rating = models.IntegerField(
        null=False,
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(0)],
        verbose_name="Рейтинг",
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
    )

    objects = models.Manager()
    published_book = PublishedBookManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book", kwargs={"book_slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = translate_to_english(self.title)
        super().save(*args, **kwargs)


class Genre(models.Model):
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    genre = models.CharField(max_length=50, db_index=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.genre

    def get_absolute_url(self):
        return reverse("genre", kwargs={"genre_slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = translate_to_english(self.genre)
        super().save(*args, **kwargs)


class Tags(models.Model):
    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    tag = models.CharField(max_length=100, db_index=True, verbose_name="Тэг")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.tag

    def get_absolute_url(self):
        return reverse("tags", kwargs={"tag_slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = translate_to_english(self.tag)
        super().save(*args, **kwargs)


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        self.slug = translate_to_english(f"{self.name} {self.surname}")
        super().save(*args, **kwargs)
