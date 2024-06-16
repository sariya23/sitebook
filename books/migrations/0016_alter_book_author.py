# Generated by Django 5.0.6 on 2024-06-16 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0015_rename_aboba_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="author",
                to="books.author",
            ),
        ),
    ]
