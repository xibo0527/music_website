from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^$',views.Index.as_view(),name='index'),
    url('^allsinger/$', views.AllSinger.as_view(), name='allsinger'),
    url('^player/$',views.Player.as_view(),name='player'),
    url('^playerlist/$',views.Playerlist.as_view(),name='playerlist'),
]