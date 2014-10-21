from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^meeting/(?P<meeting_id>\d+)/anmeldungen/$', views.anmeldungen, name="anmeldungen"),
)
