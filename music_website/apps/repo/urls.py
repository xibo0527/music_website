from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^$',TemplateView.as_view(template_name='index1.html'),name='index'),
    url('^allmusic/$',TemplateView.as_view(template_name='allmusic.html'),name='allmusic')
]