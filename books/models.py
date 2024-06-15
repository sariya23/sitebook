from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models  # type: ignore
from django.urls import reverse  # type: ignore


class PublishedBookManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=Book.PublishStatus.PUBLISHED)


class Book(models.Model):
    class Meta:
        ordering = ["-rating", "-title"]
        indexes = [models.Index(fields=["-rating"])]

    class PublishStatus(models.IntegerChoices):
        DRAFT = (0, "Черновик")
        PUBLISHED = (1, "Опубликовано")

    genre = models.ForeignKey("Genre", on_delete=models.PROTECT, related_name="books")
    tags = models.ManyToManyField("Tags", blank=True, related_name="tags")
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    author = models.CharField(max_length=70)
    rating = models.IntegerField(
        null=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        choices=PublishStatus.choices, default=PublishStatus.PUBLISHED
    )

    objects = models.Manager()
    published_book = PublishedBookManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book", kwargs={"book_slug": self.slug})


class Genre(models.Model):
    genre = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.genre

    def get_absolute_url(self):
        return reverse("genre", kwargs={"genre_slug": self.slug})


class Tags(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.tag
