from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Singer,MusicInfo
from django.core.paginator import Paginator

# Create your views here.
class Index(LoginRequiredMixin,View):
    def get(self,request):
        hotmusic = MusicInfo.objects.all().order_by('-fans')[:5]
        newmusic = MusicInfo.objects.all().order_by('-update_time')[:8]
        kwgs = {
            'hotmusic':hotmusic,
            'newmusic':newmusic,
        }
        return render(request, 'index.html',kwgs)

class AllSinger(LoginRequiredMixin,View):
    def get(self,request):
        category = request.GET.get('category','0')
        pagesize = 60
        page_num = request.GET.get('page', 1)
        if category == '0':
            objects = Singer.objects.all().order_by('-fans')
        else:
            objects = Singer.objects.filter(category=category).order_by('-fans')
        p = Paginator(objects, pagesize)
        contacts = p.page(page_num)
        kwgs = {
            'contacts': contacts,
            'category': category,
        }
        return render(request,'allsinger.html',kwgs)

from .forms import CommentsForm
class Test(View):
    def get(self,request):
        form = CommentsForm()
        return render(request,'test.html',{'form':form})