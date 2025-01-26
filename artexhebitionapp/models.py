from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Art(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="artist")
    exhibition = models.ForeignKey("Exhibition", on_delete=models.CASCADE, related_name="exhibition")

class Artist(models.Model):
    TYPES = [
        ("IM", "Impressionism"),
        ("PA", "Pop Art"),
        ("GR", "Graffiti"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="arts")
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    art_style = models.CharField(max_length=2, choices=TYPES)


class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

