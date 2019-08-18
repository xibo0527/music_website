from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^$',views.Index.as_view(),name='index'),
    url('^allsinger/$', views.AllSinger.as_view(), name='allsinger')
]