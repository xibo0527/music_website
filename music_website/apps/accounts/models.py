from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(verbose_name='手机号码',max_length=11)
    avator = models.ImageField(verbose_name='用户头像',upload_to='avator/',default='avator/default.jpg')

