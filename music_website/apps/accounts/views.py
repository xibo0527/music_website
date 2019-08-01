from django.shortcuts import render,redirect
from .forms import RegistForm,LoginForm
from django.views.generic import View
from django.contrib import messages
# Create your views here.

class Regist(View):
    def get(self,request):
        form = RegistForm()
        return render(request,'regist1.html',{'form':form})
    # msg = ''
    # reg_form = RegistForm()
    # if request.method == 'POST':
    #     reg_form = RegistForm(request.GET)
    #     if reg_form.is_valid():
    #         print('合法')
    #         return redirect('index.html')
    #     else:
    #         print('不合法')
    #         messages.add_message(request,messages.INFO,'不合法')
    #         msg='xxx不合法'
    # kwgs = {
    #     'form':reg_form,
    #     'msg':msg
    # }
    # return render(request,'regist1.html',kwgs)

class Login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login1.html',{'form':form})

def test(request):
    reg_form = RegistForm(request.GET)
    # if request.method == 'POST':
    #     reg_form = RegistForm(request.POST)
    #     if reg_form.is_valid():

    return render(request,'test.html',{'form':reg_form})