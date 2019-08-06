from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('^song$',TemplateView.as_view(template_name='song_detail.html'),name='song'),
    url('^song_list$',TemplateView.as_view(template_name='song_list_detail.html'),name='song_list'),
]
