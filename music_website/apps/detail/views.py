from django.shortcuts import render
from django.views.generic import View
from apps.repo.models import Singer,MusicInfo,SingerCollection,SongCollection,SongComments,SongCommentsDianZan
from django.core.paginator import Paginator
from apps.repo.forms import CommentsForm
from django.http import JsonResponse
# Create your views here.

class SingerDetail(View):
    def get(self,request,id):
        pagesize = 10
        page_num = request.GET.get('page', 1)
        singer = Singer.objects.get(singer_mid=id)
        music = MusicInfo.objects.filter(singer_id=id)
        p = Paginator(music, pagesize)
        music = p.page(page_num)
        fans = singer.singer_collection_set.filter(status=True).count()
        status = SingerCollection.objects.filter(user=request.user,status=True,singer=singer)
        kwgs = {
            'singer':singer,
            'music':music,
            'fans':fans,
            'status':status,
        }
        return render(request,'singer_detail.html',kwgs)

import datetime
class SongDetail(View):
    def get(self,request,id):
        status_dianzan_dic = {}
        status_dianzan_dic1 = {}
        form = CommentsForm()
        music = MusicInfo.objects.get(id=id)
        status = SongCollection.objects.filter(user=request.user, status=True,music=music)
        latestcomments = SongComments.objects.filter(song_id=id).order_by('-create_time')[:5]
        goodcomments = SongComments.objects.filter(song_id=id).order_by('-nice')[:10]
        count = SongComments.objects.filter(song_id=id).count()
        for comments in latestcomments:
            status_dianzan = SongCommentsDianZan.objects.filter(comment=comments,user=request.user,status=True)
            status_dianzan_dic[comments] = status_dianzan
        for comments in goodcomments:
            status_dianzan = SongCommentsDianZan.objects.filter(comment=comments,user=request.user,status=True)
            status_dianzan_dic1[comments] = status_dianzan
        print(status_dianzan_dic)
        print(status_dianzan_dic1)
        kwgs = {
            'music':music,
            'status':status,
            'form':form,
            # 'latestcomments':latestcomments,
            # 'goodcomments':goodcomments,
            'count':count,
            'status_dianzan_dic':status_dianzan_dic,
            'status_dianzan_dic1':status_dianzan_dic1
        }
        return render(request,'song_detail.html',kwgs)

    def post(self,request,id):
        ret = {'code':200,'msg':'提交成功'}
        if request.is_ajax():
            form = CommentsForm(request.POST)
            if form.is_valid():
                print('is valid')
                content = form.cleaned_data['content']
                print(content)
                create_time = datetime.datetime.utcnow()+datetime.timedelta(hours=8)
                SongComments.objects.create(user=request.user,song_id=id,content=content,create_time=create_time)
            else:
                print('不合法')
                ret = {'code':400,'msg':'表单数据不合法'}
        else:
            ret = {'code':400,'msg':'请求方式错误'}
        return JsonResponse(ret)