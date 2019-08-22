from django.contrib import admin
from .models import MusicInfo,Singer,SingerCategory,SongCategory,SongComments,MusicListInfo
# Register your models here.
admin.site.register(MusicInfo)
admin.site.register(MusicListInfo)
admin.site.register(Singer)
admin.site.register(SingerCategory)
admin.site.register(SongCategory)
admin.site.register(SongComments)