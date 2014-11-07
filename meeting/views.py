from django.shortcuts import get_object_or_404, render
from django.views import generic
from meeting.models import Meeting
from main.models import Start

class Index(generic.ListView):
    model = Meeting
    context_object_name = "meetings"
    template_name = "meeting/index.html"

class Detail(generic.DetailView):
    model = Meeting
    template_name = "meeting/detail.html"

def anmeldungen(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
    anmeldungen = meeting.anmeldungen.all()
    context = dict(meeting_name=meeting_name, anmeldungen=anmeldungen)
    return render(request, "meeting/anmeldungen.html", context)

def wettkaempfe(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
    wettkaempfe = dict()
    for wettkampf in meeting.wettkaempfe.all():
        wettkampf_name = "%s (%s)" % (wettkampf.info, wettkampf.kategorie.name)
        try:
            wettkaempfe[wettkampf_name]
        except KeyError:
            wettkaempfe[wettkampf_name] = []
        wettkaempfe[wettkampf_name].append(wettkampf)
    context = dict(meeting_id=meeting_id, meeting_name=meeting_name,
                   wettkaempfe=wettkaempfe)
    return render(request, "meeting/wettkaempfe.html", context)


def rangliste(request, meeting_id, wettkampf_info, kategorie_name):
    meeting_starts = Start.objects.filter(wettkampf__meeting_id=meeting_id)
    starts = meeting_starts.filter(wettkampf__info=wettkampf_info,
                                   wettkampf__kategorie__name=kategorie_name)
    resultate = dict()
    for start in starts:
        try:
            resultate[start.anmeldung.athlet]
        except KeyError:
            resultate[start.anmeldung.athlet] = dict()
        try:
            resultate[start.anmeldung.athlet][start.wettkampf.punkteformel] = \
                dict(leistung=start.serienstart.first().resultat.first().leistung,
                     wind=start.serienstart.first().serie.wind,
                     punkte=start.serienstart.first().resultat.first().punkte)
        except AttributeError:
            pass

    context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                   kategorie_name=kategorie_name, resultate=resultate)
    return render(request, "meeting/rangliste.html", context)
