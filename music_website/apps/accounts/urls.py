from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('regist/$',views.Regist.as_view(),name='regist'),
    url('login/$',views.Login.as_view(),name='login'),
    url('logout/$',views.logout,name='logout'),
]
