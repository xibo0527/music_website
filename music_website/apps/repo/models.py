from django.db import models
from apps.accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
# Create your models here.



class SongCategory(models.Model):
    name = models.CharField("分类名称", max_length=64)
    class Meta:
        verbose_name = '歌曲分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class SingerCategory(models.Model):
    name = models.CharField("分类名称", max_length=64)
    class Meta:
        verbose_name = '歌手分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Singer(models.Model):
    name = models.CharField(verbose_name='歌手名',max_length=64)
    img = models.CharField(verbose_name='歌手图片',max_length=254,null=True)
    area = models.CharField(verbose_name='地区',max_length=32,null=True)
    singer_mid = models.CharField(verbose_name='歌手id',max_length=64,primary_key=True)
    category = models.ForeignKey(SingerCategory,verbose_name='歌手类别')
    fans = models.IntegerField(verbose_name='粉丝数',default=0)


    class Meta:
        verbose_name = '歌手表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class MusicInfo(models.Model):

    name = models.CharField(verbose_name='歌曲名',max_length=254)
    singer = models.ForeignKey(Singer,verbose_name='歌手')
    song_id = models.CharField(verbose_name='音乐id', max_length=32,null=True)
    url = models.CharField(verbose_name='歌曲链接',max_length=254,null=True)
    img = models.CharField(verbose_name='歌曲图片链接',max_length=254,null=True)
    lyric = models.CharField(verbose_name='歌曲歌词链接',max_length=254,null=True)
    update_time = models.DateTimeField(verbose_name='歌曲上线时间',auto_now_add=True,null=True)
    song_count = models.IntegerField(verbose_name='歌曲被点击的次数',default=0,null=True)
    category = models.ForeignKey(SongCategory, verbose_name='歌曲类别')
    fans = models.IntegerField(verbose_name='被收藏数',default=0)

    class Meta:
        verbose_name = '音乐库'
        verbose_name_plural = verbose_name
        ordering = ['-fans']

    def __str__(self):
        return self.name



class SingerCollection(models.Model):
    singer = models.ForeignKey(Singer,verbose_name='歌手',related_name='singer_collection_set')
    user = models.ForeignKey(User,verbose_name='收藏者',related_name='singer_collection_set')
    status = models.BooleanField("收藏状态", default=True)

    class Meta:
        verbose_name = "歌手收藏表"
        verbose_name_plural = verbose_name


    def __str__(self):
        if self.status: ret="收藏"
        else: ret="没有收藏"
        return f"{self.user.username}:{ret}:{self.singer.name}"

class SongCollection(models.Model):
    music = models.ForeignKey(MusicInfo,verbose_name='歌曲',related_name='song_collection_set')
    user = models.ForeignKey(User,verbose_name='收藏者',related_name='song_collection_set')
    status = models.BooleanField("收藏状态", default=True)

    class Meta:
        verbose_name = "歌曲收藏表"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status: ret="收藏"
        else: ret="没有收藏"
        return f"{self.user.username}:{ret}:{self.music.name}"

class SongComments(models.Model):
    song = models.ForeignKey(MusicInfo,verbose_name='歌曲',related_name='songs_comment_set')
    user = models.ForeignKey(User, verbose_name='评论者', related_name='songs_comment_set')
    content = RichTextUploadingField(verbose_name='评论内容',max_length=254)
    nice = models.IntegerField(verbose_name='点赞数',default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '歌曲评论表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user.username}-{self.song.name}'

class SongCommentsDianZan(models.Model):
    user = models.ForeignKey(User, verbose_name='点赞者', related_name='dianzan_set')
    comment = models.ForeignKey(SongComments,verbose_name='评论',related_name='dianzan_set')
    status = models.BooleanField("点赞状态", default=True)

    class Meta:
        verbose_name = '点赞表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user.username}-{self.comment.content}'

class MusicListInfo(models.Model):
    name = models.CharField(verbose_name='歌单名',max_length=32)
    song = models.ManyToManyField(MusicInfo,verbose_name='歌曲')
    user = models.ForeignKey(User,verbose_name='创建者')
    img = ThumbnailerImageField(verbose_name='歌单图片',upload_to='songListimg/%Y%m%d/',default='songListimg/default.jpg')
    update_time = models.DateTimeField(verbose_name='歌单创建时间',auto_now_add=True)
    fans = models.IntegerField(verbose_name='被收藏数',default=0)

    class Meta:
        verbose_name = '歌单表'
        verbose_name_plural =verbose_name
        ordering = ['-fans']

    def __str__(self):
        return self.name

class MusicListCollection(models.Model):
    name = models.ForeignKey(MusicListInfo,verbose_name='歌单',related_name='musiclist_collection_set')
    user = models.ForeignKey(User,verbose_name='收藏者',related_name='musiclist_collection_set')
    status = models.BooleanField("收藏状态", default=True)

    class Meta:
        verbose_name = "歌单收藏表"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status: ret="收藏"
        else: ret="没有收藏"
        return f"{self.user.username}:{ret}:{self.name.name}"