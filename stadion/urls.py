from django.conf.urls import patterns, url

from stadion import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<stadion_id>\d+)/$', views.details, name='details'),
    url(r'^(?P<stadion_id>\d+)/vote/$', views.vote, name='vote'),
)
