from django.http import JsonResponse
from common.constant import base_url

def dummy_game_list(request):
    base_image_url = f"{base_url}static/images/"

    games = [
        {
            "image": f"{base_image_url}game_{i}.jpg",  # Use numbered images like game_1.jpg, game_2.jpg, etc.
            "name": f"Game {i}",
            "nextGameTime": f"{10 + i}:00 AM",  # Example: 10:00 AM, 11:00 AM, etc.
            "totalPlayers": 100 + (i * 50),  # Example: 100, 150, 200, etc.
            "prizeAmount": 1000.0 + (i * 500),  # Example: 1000.0, 1500.0, 2000.0, etc.
            "gameType": f"Type {chr(65 + i)}",  # Example: Type A, Type B, Type C, etc.
        }
        for i in range(1, 6)  # Generate 5 games
    ]

    return JsonResponse(games, safe=False)