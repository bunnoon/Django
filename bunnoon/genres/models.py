from django.db import models

# Create your models here.


class Genre(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(null=True, blank=True)
    deletedAt = models.DateTimeField(null=True, blank=True)
    genrePk = models.CharField(max_length=40, unique=True)
    enName = models.CharField(max_length=40)
    thName = models.CharField(max_length=40)
