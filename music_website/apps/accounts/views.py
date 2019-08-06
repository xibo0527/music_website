from django.shortcuts import render,HttpResponse,reverse,redirect
from django.views.generic import View
import logging
from .forms import RegistForm, LoginForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.http import JsonResponse
from django.core.cache import cache
# Create your views here.
logger = logging.getLogger('account')

class Regist(View):
    def get(self,request):
        form = RegistForm()
        return render(request,'regist1.html',{'form':form})
    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误"}
        # 检查是不是ajax的请求
        if request.is_ajax():
            form = RegistForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                mobile = form.cleaned_data["mobile"]
                mobile_captcha = form.cleaned_data["mobile_captcha"]
                mobile_captcha_reids = cache.get(mobile)
                if mobile_captcha == mobile_captcha_reids:
                    user = User.objects.create(username=username, password=make_password(password))
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    logger.debug(f"新用户{user}注册成功！")
                    user = auth.authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        logger.debug(f"新用户{user}登录成功")
                    else:
                        logger.error(f"新用户{user}登录失败")
                else:
                    # 验证码错误
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
                # ret['msg'] = '请将注册表格填完整'
        logger.debug(f"用户注册结果：{ret}")
        return JsonResponse(ret)



class Login(View):
    def get(self, request):
        request.session['next'] = request.GET.get('next', reverse('repo:index'))
        if request.user.is_authenticated:
            return redirect(request.session['next'])
        form = LoginForm()
        return render(request, 'login1.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            captcha = form.cleaned_data["captcha"]
            session_captcha_code = request.session.get("captcha_code", "")
            logger.debug(f"登录提交验证码:{captcha}-{session_captcha_code}")
            # 验证码一致
            if captcha.lower() == session_captcha_code.lower():
                user, flag = form.check_password()
                # user = auth.authenticate(username=username, password=password)
                if flag and user and user.is_active:
                    auth.login(request, user)
                    logger.info(f"{user.username}登录成功")
                    # 跳转到next
                    return redirect(request.session.get("next", '/'))
                msg = "用户名或密码错误"
                logger.error(f"{username}登录失败, 用户名或密码错误")
            else:
                msg = "验证码错误"
                logger.error(f"{username}登录失败, 验证码错误")
        else:
            msg = "表单数据不完整"
            logger.error(msg)
        return render(request, "login1.html", {"form": form, "msg": msg})

def logout(request):
    auth.logout(request)
    return redirect(reverse('repo:index'))