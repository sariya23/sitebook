from django.db import models
from django.urls import reverse


class PublishedBookManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=1)
    

class Book(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    author = models.CharField(max_length=70)
    rating = models.IntegerField(null=False, default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    objects = models.Manager()
    published_book = PublishedBookManager()

    class Meta:
        ordering = ["-rating", "-title"]
        indexes = [
            models.Index(fields=["-rating"])
        ]



    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("book", kwargs={"book_slug": self.slug})