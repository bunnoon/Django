from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpRequest
from .models import Anime

# Create your views here.


class AnimeDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request: HttpRequest, pk: str):
        try:
            anime = Anime.objects.get(animePk=pk)
            return Response({
                'success': True,
                'status': 200,
                'data': {
                    'anime': {
                        'name': {
                            'en': anime.enName,
                            'th': anime.thName,
                        }
                    }
                }
            })
        except Anime.DoesNotExist:
            return Response({
                'success': False,
                'status': 404,
                'error': 'anime not found!'
            })
        except:
            return Response({
                'success': False,
                'status': 500,
                'error': 'internal server error!'
            })
