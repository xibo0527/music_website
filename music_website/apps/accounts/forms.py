from django import forms
from django.forms import widgets

class RegistForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=widgets.TextInput(attrs={"class":"form-control rounded input-lg text-center no-border",'placeholder':'设置用户名'}),
                               error_messages={
                                   'required':'请输入用户名'
                               }
                               )
    mobile = forms.CharField(label='电话号码',
                                  widget=widgets.TextInput(attrs={"class":"form-control rounded input-lg text-center no-border",'placeholder':'输入电话号码'}))
    password = forms.CharField(label='输入密码',
                               max_length=18,
                               min_length=8,
                                widget=forms.PasswordInput(attrs={"class":"form-control rounded input-lg text-center no-border",'placeholder':'设置密码'}))
    password2 = forms.CharField(label='确认密码',
                               max_length=18,
                               min_length=8,
                               widget=forms.PasswordInput(attrs={"class":"form-control rounded input-lg text-center no-border",'placeholder':'确认密码'}))
    mobil_captcha = forms.CharField(label='输入验证码',
                                  widget=widgets.TextInput(attrs={"class":"form-control rounded input-lg text-center no-border",'placeholder':'输入验证码',"style":"width:200px;"}))

class LoginForm(forms.Form):
    mobile = forms.CharField(label="手机号码", max_length="24",
                               widget=widgets.TextInput(attrs={"class":"form-control rounded input-lg text-center no-border", "placeholder": "手机号码"}))
    captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={"style": "width: 160px", "class":"form-control rounded input-lg text-center no-border","placeholder": "验证码", "onblur": "check_captcha()",
               "error_messages": {"invalid": "验证码错误"}}))
    password = forms.CharField(label="密 码",
                               widget=widgets.PasswordInput(attrs={"class":"form-control rounded input-lg text-center no-border", "placeholder": "请输入密码"}))