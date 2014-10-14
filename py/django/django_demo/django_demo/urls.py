from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_demo.views.home', name='home'),

    url(r'^vip/', include('vip.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
