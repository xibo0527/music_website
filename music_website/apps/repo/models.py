from django.db import models
from apps.accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField
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
    # song_comments = models.ManyToManyField(User,verbose_name='歌曲评论', max_length=254)

    class Meta:
        verbose_name = '音乐库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# class MusicListInfo(models.Model):
#     song_list_name = models.CharField(verbose_name='歌单名',max_length=254)
#     song_list_url = models.CharField(verbose_name='歌单链接',max_length=254)
#     song_list_img = models.CharField(verbose_name='歌单图片链接',max_length=254,default='img/xxx')
#     update_time = models.DateTimeField(verbose_name='歌单上线时间',auto_now_add=True)
#     song_list_count = models.IntegerField(verbose_name='歌单被点击的次数')
#
#     song_list_class = models.IntegerField(verbose_name='歌单类别', choices=SONG_TYPE)
#     song_list_comments = models.ManyToManyField(User,verbose_name='歌单评论', max_length=254)
#     song_list_music = models.ManyToManyField(MusicInfo,verbose_name='歌单音乐表')
#     # creater = models.ForeignKey(User,verbose_name='创建歌单的用户')
#
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
    song = models.ForeignKey(MusicInfo,verbose_name='音乐',related_name='songs_comment_set')
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