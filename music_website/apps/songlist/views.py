from django.shortcuts import render
from django.views.generic import View
from apps.repo.models import MusicListInfo,MusicInfo,MusicListCollection
from django.core.paginator import Paginator
# Create your views here.

class SongList(View):
    def get(self,request):
        music_list = MusicListInfo.objects.all().order_by('-fans')[:12]
        kwgs = {
            'music_list':music_list
        }
        return render(request,'songlist.html',kwgs)

class SongListDetail(View):
    def get(self,request,id):
        pagesize = 10
        page_num = request.GET.get('page', 1)
        music_list = MusicListInfo.objects.get(id=id)
        music = MusicInfo.objects.filter(musiclistinfo=music_list)
        p = Paginator(music, pagesize)
        music = p.page(page_num)
        # fans = music_list.musiclist_collection_set.filter(status=True).count()
        fans = music_list.fans
        status = MusicListCollection.objects.filter(user=request.user, status=True, name=music_list)
        kwgs = {
            'music_list':music_list,
            'music':music,
            'fans': fans,
            'status': status,
        }

        return render(request,'songlist_detail.html',kwgs)