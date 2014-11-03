from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse


def index(request):
    return HttpResponse("""
<nav>
  <ul>
    <li><a href="/admin">Administration</a></li>
    <li><a href="/stadion">Stadien</a></li>
    <li><a href="/meeting">Meetings</a></li>
    <li><a href="/main">Main</a></li>
  </ul>
</nav>
""")


urlpatterns = patterns(
    '',
    url(r'^$', index, name='root-index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls', namespace="main")),
    url(r'^meeting/', include('meeting.urls', namespace="meeting")),
    url(r'^stadion/', include('stadion.urls', namespace="stadion")),
)
