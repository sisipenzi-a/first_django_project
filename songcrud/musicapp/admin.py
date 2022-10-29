from django.contrib import admin

# Register your models here.
from . import models

class MusicappAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Artiste, MusicappAdmin)
admin.site.register(models.Song, MusicappAdmin) 
admin.site.register(models.Lyric, MusicappAdmin)