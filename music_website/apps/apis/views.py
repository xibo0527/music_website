from django.shortcuts import render,HttpResponse
from libs import sms
import random
from django.core.cache import cache
import logging
from django.http import JsonResponse
from django.views.generic import View,DetailView
from apps.repo.models import Singer,SingerCollection,MusicInfo,SongCollection,SongComments,SongCommentsDianZan,MusicListInfo,MusicListCollection
from django.core.paginator import Paginator
import datetime
import os
from music_website.settings import MEDIA_ROOT, MEDIA_URL
import time
from django.forms.models import model_to_dict



# Create your views here.
logger = logging.getLogger('apis')

def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        # 将短信验证码写入redis, 300s 过期
        cache.set(mobile, mobile_captcha, 300)
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "验证码发送失败！"}
    return JsonResponse(ret)

from io import BytesIO
from libs import patcha
import base64


def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = patcha.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type + base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)

def check_captcha(request):
    ret = {"code":400, "msg":"验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code',)
    session_captcha_code = request.session.get('captcha_code',)
    print(post_captcha_code, session_captcha_code)
    if post_captcha_code and post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
    return JsonResponse(ret)


class ChangeAvator(View):
    def post(self,request):
        today = datetime.date.today().strftime("%Y%m%d")
        # 图片的data-img格式=>data:image/jpg;base64,xxxx
        img_src_str = request.POST.get("image")
        # 取出数据
        img_str = img_src_str.split(',')[1]
        # 取出格式:jpg/png...
        img_type = img_src_str.split(';')[0].split('/')[1]
        # 将数据转化为bytes格式
        img_data = base64.b64decode(img_str)
        # 相对上传路径: 头像上传的相对路径
        avator_path = os.path.join("avator", today)
        # 绝对上传路径：头像上传的绝对路径
        avator_path_full = os.path.join(MEDIA_ROOT, avator_path)
        if not os.path.exists(avator_path_full):
            os.mkdir(avator_path_full)
        filename = str(time.time()) + "." + img_type
        # 绝对文件路径，用于保存图片
        filename_full = os.path.join(avator_path_full, filename)
        # 相对MEDIA_URL路径，用于展示数据
        img_url = f"{MEDIA_URL}{avator_path}/{filename}"
        try:
            with open(filename_full, 'wb') as fp:
                fp.write(img_data)
            ret = {
                "result": "ok",
                "file": img_url
            }
        except Exception as ex:
            ret = {
                "result": "error",
                "file": "upload fail"
            }

        request.user.avator = os.path.join(avator_path, filename)
        request.user.save()
        return JsonResponse(ret)

class UpdateAvator(View):
    def get(self,request):
        avator_url = request.user.avator['avatar'].url
        ret = {'code': 200,'avator_url':avator_url}
        return JsonResponse(ret)

class SingerCollect(View):
    def get(self,request,id):
        singer = Singer.objects.get(singer_mid=id)

        result = SingerCollection.objects.get_or_create(user=request.user,singer=singer)
        singer_collection = result[0]
        if not result[1]:
            if singer_collection.status:
                singer_collection.status = False
                singer.fans = singer.fans-1
            else:
                singer_collection.status = True
                singer.fans = singer.fans + 1
        else:
            singer.fans = singer.fans + 1
        singer.save()
        singer_collection.save()
        # fans = singer.singer_collection_set.filter(status=True).count()
        fans = singer.fans
        msg = model_to_dict(singer_collection)
        ret = {
            'code':200,'msg':msg,'fans':fans
        }
        return JsonResponse(ret)

class SongCollect(View):
    def get(self,request,id):
        music = MusicInfo.objects.get(id=id)
        result = SongCollection.objects.get_or_create(user=request.user,music=music)
        song_collection = result[0]
        if not result[1]:
            if song_collection.status:
                song_collection.status = False
                music.fans = music.fans - 1
            else:
                song_collection.status = True
                music.fans = music.fans + 1
        else:
            music.fans = music.fans + 1
        music.save()
        song_collection.save()
        msg = model_to_dict(song_collection)
        ret = {
            'code':200,'msg':msg
        }
        return JsonResponse(ret)

class DianZan(View):
    def get(self,request,id):
        comment = SongComments.objects.get(id=id)
        result = SongCommentsDianZan.objects.get_or_create(user=request.user,comment=comment)
        comment_dianzan = result[0]
        if not result[1]:
            if comment_dianzan.status:
                comment_dianzan.status = False
                comment.nice = comment.nice - 1
            else:
                comment_dianzan.status = True
                comment.nice = comment.nice + 1
        else:
            comment.nice = comment.nice + 1
        comment.save()
        comment_dianzan.save()
        msg = model_to_dict(comment_dianzan)
        msg1 = model_to_dict(comment)
        ret = {
            'code':200,'msg':msg,'msg1':msg1
        }
        return JsonResponse(ret)

class SongListCollect(View):
    def get(self,request,id):
        music_list = MusicListInfo.objects.get(id=id)
        result = MusicListCollection.objects.get_or_create(user=request.user, name=music_list)
        music_list_collection = result[0]
        if not result[1]:
            if music_list_collection.status:
                music_list_collection.status = False
                music_list.fans = music_list.fans - 1
            else:
                music_list_collection.status = True
                music_list.fans = music_list.fans + 1
        else:
            music_list.fans = music_list.fans + 1
        music_list.save()
        music_list_collection.save()
        # fans = music_list.musiclist_collection_set.filter(status=True).count()
        fans = music_list.fans
        msg = model_to_dict(music_list_collection)
        ret = {
            'code': 200, 'msg': msg, 'fans': fans
        }
        return JsonResponse(ret)

class ToSongList(View):
    def post(self,request,id):
        songlistid = request.POST.get('songlistid')
        song = MusicInfo.objects.filter(id=id)
        songlist = MusicListInfo.objects.get(id=songlistid)
        songs = MusicInfo.objects.filter(musiclistinfo=songlist)
        songlist.song = song | songs
        songlist.save()
        ret = {
            'code':200
        }
        return JsonResponse(ret)