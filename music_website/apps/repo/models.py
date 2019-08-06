from django.db import models
from apps.accounts.models import User
# Create your models here.
SONG_TYPE = (
    (1,'流行'),
    (2,'民谣'),
    (3,'英语'),
    (4,'轻音乐'),
)

class MusicInfo(models.Model):
    song_name = models.CharField(verbose_name='歌曲名',max_length=254)
    song_url = models.CharField(verbose_name='歌曲链接',max_length=254)
    song_img = models.CharField(verbose_name='歌曲图片链接',max_length=254,default='img/xxx')
    song_lyric = models.CharField(verbose_name='歌曲歌词链接',max_length=254,default='lyric/xxx')
    song_class = models.IntegerField(verbose_name='歌曲类别',choices=SONG_TYPE)
    update_time = models.DateTimeField(verbose_name='歌曲上线时间',auto_now_add=True)
    song_count = models.IntegerField(verbose_name='歌曲被点击的次数')

    song_comments = models.ManyToManyField(User,verbose_name='歌曲评论', max_length=254)

class MusicListInfo(models.Model):
    song_list_name = models.CharField(verbose_name='歌单名',max_length=254)
    song_list__url = models.CharField(verbose_name='歌单链接',max_length=254)
    song_list_img = models.CharField(verbose_name='歌单图片链接',max_length=254,default='img/xxx')
    song_list_class = models.IntegerField(verbose_name='歌单类别',choices=SONG_TYPE)
    update_time = models.DateTimeField(verbose_name='歌单上线时间',auto_now_add=True)
    song_list_count = models.IntegerField(verbose_name='歌单被点击的次数')

    song_list_comments = models.ManyToManyField(User,verbose_name='歌单评论', max_length=254)
    song_list_music = models.ForeignKey(MusicInfo,verbose_name='音乐表')