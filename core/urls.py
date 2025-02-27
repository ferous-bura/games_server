from django.urls import path, include
from .download_files import download_game

urlpatterns = [
    path('', include('core.api.urls')),
    path('game', download_game, name='download_game'),
]
