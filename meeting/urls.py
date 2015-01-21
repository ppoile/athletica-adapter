from django.conf.urls import patterns, url

from meeting import views

urlpatterns = patterns(
    '',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    url(r'^(?P<meeting_id>\d+)/anmeldungen/$', views.anmeldungen, name='anmeldungen'),
    url(r'^(?P<meeting_id>\d+)/wettkaempfe/$', views.wettkaempfe, name='wettkaempfe'),
    url(r'^(?P<meeting_id>\d+)/wettkaempfe/(?P<wettkampf_info>.+?)/(?P<kategorie_name>.+?)/rangliste/$', views.rangliste, name='rangliste'),
    url(r'^(?P<meeting_id>\d+)/wettkaempfe/(?P<wettkampf_info>.+?)/(?P<kategorie_name>.+?)/rangliste-odt/$', views.rangliste_odt, name='rangliste-odt'),
    url(r'^(?P<meeting_id>\d+)/zeitplan/$', views.zeitplan, name='zeitplan'),
)
