from django.db import models


class BingoGame(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=255)
    next_game_time = models.CharField(max_length=50)
    total_players = models.IntegerField()
    prize_amount = models.DecimalField(max_digits=10, decimal_places=2)
    game_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name