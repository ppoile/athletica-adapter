from django.conf.urls import patterns, url

from meeting import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    url(r'^(?P<meeting_id>\d+)/anmeldungen/$', views.anmeldungen, name='anmeldungen'),
)
