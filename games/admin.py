from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'upload_date')
    search_fields = ('title', 'category')
    list_filter = ('category', 'upload_date')
