from django.http import HttpRequest
from django.shortcuts import render
from .models import Anime

# Create your views here.


def animes(request: HttpRequest):
    queryset = Anime.objects.all()
    return render(request, 'ListAnime.html', {
        'success': True,
        'status': 200,
        'title': 'Anime List Page',
        'data': queryset,
    })


def anime(request: HttpRequest, pk: str, title: str):
    try:
        queryset = Anime.objects.get(animePk=pk)
        return render(request, 'ViewAnime.html', {
            'success': True,
            'status': 200,
            'title': 'Anime View Page',
            'data': queryset,
        })
    except Anime.DoesNotExist:
        return render(request, 'ViewAnime.html', {
            'success': False,
            'status': 404,
        })
