from django.shortcuts import render, redirect
from django import forms
from .models import Game, Rating

def upload_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("game_list")  # После загрузки перекидывает на список игр
    else:
        form = GameForm()
    return render(request, "games/upload_game.html", {"form": form})

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["title", "description", "cover", "torrent_file", "direct_link", "category"]