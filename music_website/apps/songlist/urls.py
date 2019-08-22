from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^$',views.SongList.as_view(),name='songlist'),
    url('^(?P<id>\d+)/$',views.SongListDetail.as_view(),name='songlistdetail')
]
