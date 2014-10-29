from django.conf.urls import patterns, url

from stadion import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.CreateView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
)
