from django.shortcuts import get_object_or_404, render
from django.views import generic
from meeting.models import Meeting
from main.models import Start
from meeting.rangliste import RanglistenItem, Rangliste


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
    # resultate = {
    #     "Hans Muster": {
    #         "punkte_total": 1234,
    #         "resultate": {
    #             100: {leistung: 9.81, wind: -0.3, punkte: 333}
    #             WEIT: {leistung: 6.05, wind: +1.0, punkte: 733}
    #         }
    #     }
    # }
    #
    # rangliste = [<rang>, <name> <vorname>, <jahrgang>, <verein>, <land>,
    #              <punkte>, <bemerkung>, <resultate>]

    meeting_starts = Start.objects.filter(wettkampf__meeting_id=meeting_id)
    starts = meeting_starts.filter(wettkampf__info=wettkampf_info,
                                   wettkampf__kategorie__name=kategorie_name)
    ordered_starts = starts.order_by("anmeldung__athlet")
    rangliste = Rangliste()
    for start in ordered_starts:
        rangliste.addStart(start)

    context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                   kategorie_name=kategorie_name, rangliste=rangliste)
    return render(request, "meeting/rangliste.html", context)
