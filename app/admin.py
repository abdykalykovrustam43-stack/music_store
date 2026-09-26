from django.contrib import admin

from .models import Sound


@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'genre',
        'price',
        'created_at',
    )