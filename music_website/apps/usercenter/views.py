from django.shortcuts import render
from django.views.generic import View,ListView
from django.http import JsonResponse
from apps.repo.models import MusicInfo,SongCollection,MusicListInfo,Singer
from django.core.paginator import Paginator

# Create your views here.
class Profile(View):
    def get(self,request):
        ret = {'sex':'保密'}
        sex = request.user.sex
        if sex == 3:
            ret = {'sex':'男'}
        elif sex == 1:
            ret = {'sex':'女'}
        return render(request,'uc_profile.html',ret)
    def post(self,request):
        try:
            email = request.POST.get('email','')
            desc = request.POST.get('desc','这个人很懒，什么都没留下')
            mobile = request.POST.get('mobile','')
            sex = request.POST.get('sex',2)
            request.user.email = email
            request.user.desc = desc
            request.user.mobile = mobile
            request.user.sex = sex
            request.user.save()
            kwgs = {
                'email': email,
                'desc': desc,
                'mobile': mobile,
                'sex': sex,
            }
            ret = {"code": 200, "msg": "修改成功", 'userinfo': kwgs}
        except Exception as f:
            ret = {'code':400,'msg':'修改失败，请联系管理员'}
        return JsonResponse(ret)

class ChangePasswdView(View):
    def get(self,request):
        return render(request, "uc_change_passwd.html")

class MyMusic(View):
    def get(self,request):
        pagesize = 5
        page_num = request.GET.get('page', 1)
        mymusic = MusicInfo.objects.filter(song_collection_set__status=True, song_collection_set__user=request.user)
        p = Paginator(mymusic, pagesize)
        mymusic = p.page(page_num)
        kwgs = {
            'mymusic':mymusic
        }
        return render(request,'mymusic.html',kwgs)

class MyMusicList(View):
    def get(self,request):
        pagesize = 5
        page_num = request.GET.get('page', 1)
        mymusiclist = MusicListInfo.objects.filter(user=request.user)
        p = Paginator(mymusiclist, pagesize)
        mymusiclist = p.page(page_num)
        kwgs = {
            'mymusiclist': mymusiclist
        }
        return render(request,'mymusiclist.html',kwgs)

class MyFocus(View):
    def get(self,request):
        pagesize = 5
        page_num = request.GET.get('page', 1)
        singer = Singer.objects.filter(singer_collection_set__status=True,singer_collection_set__user=request.user)
        p = Paginator(singer, pagesize)
        singer = p.page(page_num)
        kwgs = {
            'singer': singer
        }
        return render(request, 'myfocus.html', kwgs)