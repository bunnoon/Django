from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.genres, name='list-genre'),
    re_path(r'^(?P<pk>\S{1,50})$', views.genre, name='view-genre'),
]
