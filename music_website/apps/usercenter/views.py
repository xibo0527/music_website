from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

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
        return render(request,'mymusic.html')