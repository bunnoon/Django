from django.db import models
from animes.models import Anime

# Create your models here.


class Genre(models.Model):
    handle = models.CharField(max_length=40, unique=True)
    enName = models.CharField(max_length=40)
    thName = models.CharField(max_length=40)


class GenresToAnimes(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
