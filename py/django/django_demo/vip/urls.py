from django.conf.urls import patterns, url
from vip import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<id>\d+)/result/$', views.result, name='result'),
)