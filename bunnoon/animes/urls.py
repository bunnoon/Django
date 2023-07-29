from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.animes, name='list-anime'),
    re_path(r'^(?P<pk>\w{0,7})/(?P<title>\w{0,50})$',
            views.anime, name='view-anime'),
]
