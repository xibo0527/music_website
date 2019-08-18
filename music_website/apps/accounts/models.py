from django.db import models
from django.contrib.auth.models import AbstractUser
from easy_thumbnails.fields import ThumbnailerImageField
# Create your models here.

# from apps.repo.models import MusicInfo
SEX_CHOICES = (
    (3,'男'),
    (1,'女'),
    (2,'保密')
)

class User(AbstractUser):
    mobile = models.CharField(verbose_name='手机号码',max_length=11)
    # avator = models.ImageField(verbose_name='用户头像',upload_to='avator/',default='avator/default.jpg')
    avator = ThumbnailerImageField(verbose_name='用户头像',upload_to='avator/%Y%m%d/',default='avator/default.jpg')

    email = models.EmailField(verbose_name='邮箱', max_length=254, null=True, blank=True)
    desc = models.CharField(verbose_name='个人说明', max_length=254, null=True, blank=True)
    sex = models.IntegerField(verbose_name='性别', choices=SEX_CHOICES,default=2)

    # lovesongs = models.ManyToManyField(MusicInfo,verbose_name='喜欢的音乐表')