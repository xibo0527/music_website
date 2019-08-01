from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url('regist/$',views.Regist.as_view(),name='regist'),
    url('login/$',views.Login.as_view(),name='login'),
    url('test',views.test,name='test'),

]
