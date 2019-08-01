from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=18)
    password = models.CharField(verbose_name='密码',max_length=128)
    phonenumber = models.CharField(verbose_name='电话号码',max_length=11)

