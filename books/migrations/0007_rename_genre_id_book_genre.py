# Generated by Django 5.0.6 on 2024-06-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_alter_book_genre_id_alter_genre_genre"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="genre_id",
            new_name="genre",
        ),
    ]
