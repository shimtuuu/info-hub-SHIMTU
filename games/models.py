from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


User = get_user_model()

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to='game_covers/', blank=True, null=True)
    rating = models.FloatField(default=0)
    total_votes = models.IntegerField(default=0)
    favorites = models.ManyToManyField(User, blank=True)
    category = models.CharField(max_length=100, choices=[("Action", "Action"), ("RPG", "RPG"), ("Strategy", "Strategy")])
    direct_link = models.URLField(blank=True, null=True)
    torrent_file = models.FileField(upload_to='torrents/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_games")

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_ratings")  # 🔥 УНИКАЛЬНЫЙ related_name
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="games_ratings")  # 🔥 УНИКАЛЬНЫЙ related_name
    value = models.IntegerField()

class GameFavorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "game")

favorites = models.ManyToManyField(User, through="GameFavorites", blank=True)
