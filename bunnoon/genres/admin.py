from django.contrib import admin
from .models import Genre, GenresToAnimes

# Register your models here.
admin.site.register(Genre)
admin.site.register(GenresToAnimes)
