from django.db import models
from animes.models import Anime

# Create your models here.


class Genre(models.Model):
    handle = models.CharField(max_length=40, unique=True)
    enName = models.CharField(max_length=40)
    thName = models.CharField(max_length=40)

    def __str__(self):
        return self.enName


class GenresToAnimes(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} <-> {}'.format(self.genre.enName, self.anime.enName)
