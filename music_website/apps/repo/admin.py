from django.contrib import admin
from .models import MusicInfo,Singer,SingerCategory
# Register your models here.
admin.site.register(MusicInfo)
admin.site.register(Singer)
admin.site.register(SingerCategory)