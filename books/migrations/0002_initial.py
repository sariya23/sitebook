# Generated by Django 5.0.6 on 2024-06-21 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("books", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="creator",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="creator",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель статьи",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="books.genre",
                verbose_name="Жанр",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="books.tags", verbose_name="Тэги"
            ),
        ),
        migrations.AddIndex(
            model_name="book",
            index=models.Index(fields=["-rating"], name="books_book_rating_e5a7e2_idx"),
        ),
    ]
