from django.urls import path
from .views import game_list

urlpatterns = [
    path('api/full-data/', game_list, name='game_list'),
]