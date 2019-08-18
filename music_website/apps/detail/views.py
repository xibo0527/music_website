from django.shortcuts import render
from django.views.generic import View
from apps.repo.models import Singer
# Create your views here.

class SingerDetail(View):
    def get(self,request,id):
        singer = Singer.objects.get(singer_mid=id)
        kwgs = {
            'singer':singer
        }
        return render(request,'singer_detail.html',kwgs)