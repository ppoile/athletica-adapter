from django.conf.urls import patterns, url

from stadion import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^add/$', views.Create.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
)
