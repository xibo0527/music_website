from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^profile/$',views.Profile.as_view(),name='profile'),
    url(r'^change_passwd/$',views.ChangePasswdView.as_view(),name='change_passwd'),
    url(r'^my_music/$',views.MyMusic.as_view(),name='my_music')
]
