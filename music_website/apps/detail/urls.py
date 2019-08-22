from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^song/(?P<id>\w+)/$',views.SongDetail.as_view(),name='song'),
    url('^song_list/$',TemplateView.as_view(template_name='song_list_detail.html'),name='song_list'),
    url('^singer/(?P<id>\w+)/$',views.SingerDetail.as_view(),name='singer_detail')
]
