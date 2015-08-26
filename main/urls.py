from django.conf.urls import patterns, url
from django.http import HttpResponse
from main import views
from main.einteilung import GruppenEinteilung
from main.einteilung import SerienEinteilung
from main.meeting import MeetingDetail
from main.meeting import MeetingIndex
from main.stadion import StadionCreate
from main.stadion import StadionDelete
from main.stadion import StadionDetail
from main.stadion import StadionIndex
from main.stadion import StadionUpdate
from main.stadion import voteStadion
from main.wettkampf import WettkampfDetail
from main.wettkampf import WettkampfIndex
from main.zeitplan import MeetingZeitplan


def index(request):
    return HttpResponse("""
<nav>
  <ul>
    <li><a href=/main/meeting>Meetings</a></li>
    <li><a href=/main/stadion>Stadien</a></li>
  </ul>
</nav>
""")


urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^meeting/$', MeetingIndex.as_view(), name='meeting-index'),
    url(r'^meeting/(?P<pk>\d+)/$', MeetingDetail.as_view(),name='meeting-detail'),
    url(r'^meeting/(?P<meeting_id>\d+)/anmeldungen/$', views.anmeldungen, name='anmeldungen'),
    url(r'^meeting/(?P<meeting_id>\d+)/wettkampf/$', WettkampfIndex.as_view(), name='wettkampf-index'),
    url(r'^meeting/(?P<meeting_id>\d+)/wettkampf/(?P<wettkampf_info>.+?)/(?P<kategorie_name>.+?)/gruppen-einteilung/$', GruppenEinteilung.as_view(), name='gruppen-einteilung'),
    url(r'^meeting/(?P<meeting_id>\d+)/wettkampf/(?P<wettkampf_info>.+?)/(?P<kategorie_name>.+?)/rangliste/$', views.rangliste, name='rangliste'),
    url(r'^meeting/(?P<meeting_id>\d+)/wettkampf/(?P<wettkampf_info>.+?)/(?P<kategorie_name>.+?)/rangliste-odt/$', views.rangliste_odt, name='rangliste-odt'),
    url(r'^meeting/(?P<meeting_id>\d+)/wettkampf/(?P<wettkampf_info>.+?)/(?P<kategorie_name>.+?)/$', WettkampfDetail.as_view(), name='wettkampf-detail'),
    url(r'^meeting/(?P<meeting_id>\d+)/wettkampf/(?P<wettkampf_id>\d+?)/serien-einteilung/$', SerienEinteilung.as_view(), name='serien-einteilung'),
    url(r'^meeting/(?P<meeting_id>\d+)/zeitplan/$', MeetingZeitplan.as_view(), name='zeitplan'),
    url(r'^stadion/$', StadionIndex.as_view(), name='stadion-index'),
    url(r'^stadion/add/$', StadionCreate.as_view(), name='stadion-add'),
    url(r'^stadion/(?P<pk>\d+)/$', StadionDetail.as_view(), name='stadion-detail'),
    url(r'^stadion/(?P<pk>\d+)/delete/$', StadionDelete.as_view(), name='stadion-delete'),
    url(r'^stadion/(?P<pk>\d+)/vote/$', voteStadion, name='stadion-vote'),
)
