from django.contrib import admin
from django.apps import AppConfig
from .models import Album,Song
# Register your models here.


# class MusicConfig(AppConfig):
#     name = 'music'

admin.site.register(Album)
admin.site.register(Song)