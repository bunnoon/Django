from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def animes(request: HttpRequest):
    return render(request, 'ListAnime.html', {'title': 'Anime List Page'})


def anime(request: HttpRequest, pk: str, title: str):
    return render(request, 'ViewAnime.html', {'title': 'Anime View Page'})
