# Generated by Django 5.1.5 on 2025-01-27 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                (
                    "art_style",
                    models.CharField(
                        choices=[
                            ("IM", "Impressionism"),
                            ("PA", "Pop Art"),
                            ("GR", "Graffiti"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="arts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Art",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("creation_date", models.DateTimeField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="artist",
                        to="artexhebitionapp.artist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exhibition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("description", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                (
                    "art",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exhibition_art",
                        to="artexhebitionapp.art",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="art",
            name="exhibition",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exhibition",
                to="artexhebitionapp.exhibition",
            ),
        ),
    ]
