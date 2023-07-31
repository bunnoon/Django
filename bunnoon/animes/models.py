from django.db import models

# Create your models here.


class Anime(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(null=True, blank=True)
    deletedAt = models.DateTimeField(null=True, blank=True)
    animePk = models.CharField(max_length=7, unique=True)
    title = models.CharField(max_length=60)
    enName = models.CharField(max_length=60)
    thName = models.CharField(max_length=60)
