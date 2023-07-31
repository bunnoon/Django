from django.db import models

# Create your models here.


class Genre(models.Model):
    handle = models.CharField(max_length=40, unique=True)
    enName = models.CharField(max_length=40)
    thName = models.CharField(max_length=40)
