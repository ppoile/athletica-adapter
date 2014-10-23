from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls', namespace="main")),
    url(r'^meeting/', include('meeting.urls', namespace="meeting")),
    url(r'^stadion/', include('stadion.urls', namespace="stadion")),
)
