from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^stadion/$', views.sindex, name='sindex'),
    url(r'^stadion/(?P<stadion_id>\d+)/$', views.sdetail, name='sdetail'),

)
