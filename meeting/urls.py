from django.conf.urls import patterns, url

from meeting import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<meeting_id>\d+)/$', views.details, name='details'),
    url(r'^(?P<meeting_id>\d+)/anmeldungen/$', views.anmeldungen, name='anmeldungen'),
)
