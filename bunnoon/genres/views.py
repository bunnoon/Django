from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def genres(request: HttpRequest):
    return render(request, 'ListGenre.html', {'title': 'Genre List Page'})


def genre(request: HttpRequest, pk: str):
    return render(request, 'ViewGenre.html', {'title': 'Genre View Page'})
