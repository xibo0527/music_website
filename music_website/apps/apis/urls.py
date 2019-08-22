from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mobile_captcha/$',views.get_mobile_captcha,name='mobile_captcha'),
    url(r'^get_captcha/$',views.get_captcha,name='get_captcha'),
    url(r'^check_captcha/$',views.check_captcha,name='check_captcha'),
    url(r'^change_avator/$',views.ChangeAvator.as_view(),name='change_avator'),
    url(r'^update_avator/$',views.UpdateAvator.as_view(),name='update_avator'),
    url(r'^singer_collect/(?P<id>\w+)$',views.SingerCollect.as_view(),name='SingerCollect'),
    url(r'^song_collect/(?P<id>\d+)$',views.SongCollect.as_view(),name='SongCollect'),
    url(r'^dianzan/(?P<id>\d+)$',views.DianZan.as_view(),name='dianzan'),
    url(r'^songlist_collect/(?P<id>\w+)$',views.SongListCollect.as_view(),name='SongListCollect'),
]