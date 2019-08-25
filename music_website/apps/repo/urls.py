from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^$',views.Index.as_view(),name='index'),
    url('^allsinger/$', views.AllSinger.as_view(), name='allsinger'),
<<<<<<< HEAD
    url('^test/$',views.Test.as_view(),name='test'),
=======
>>>>>>> 9f7fb4617bdfaf93f49a3a2de2459c2be637ff45
    url('^player/$',views.Player.as_view(),name='player'),
    url('^playerlist/$',views.Playerlist.as_view(),name='playerlist'),
]