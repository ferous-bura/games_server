from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from bingo.models import BingoGame

def game_list(request):
    games = BingoGame.objects.all()
    data = [
        {
            "image": game.image,
            "name": game.name,
            "nextGameTime": game.next_game_time,
            "totalPlayers": game.total_players,
            "prizeAmount": float(game.prize_amount),  # Convert Decimal to float
            "gameType": game.game_type,
        }
        for game in games
    ]
    return JsonResponse(data, safe=False)