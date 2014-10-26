from django.conf.urls import patterns, url

from stadion import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
)
