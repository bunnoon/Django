from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.animes, name='list-anime'),
    re_path(r'^(?P<pk>\w{7})/(?P<title>\S{1,60})$',
            views.anime, name='view-anime'),
]
