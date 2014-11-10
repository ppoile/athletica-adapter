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
    resultate = dict()
    for start in starts:
        athlet = start.anmeldung.athlet
        key = "%s %s" % (athlet.name, athlet.vorname)
        try:
            resultate[key]
        except KeyError:
            resultate[key] = dict(punkte_total=0, disziplinen=dict())
        athleten_resultate = resultate[key]

        REAL_LEISTUNG_DIVISOR = {"60": 1000, "WEIT": 100, "KUGEL": 100,
                                 "HOCH": 100, "600": 1000}

        try:
            punkteformel = start.wettkampf.punkteformel
            divisor = REAL_LEISTUNG_DIVISOR[punkteformel]
            leistung = start.serienstart.first().resultat.first().leistung
            if leistung < 0:
                leistung = "%s" % leistung
                LEISTUNG_PUNKTE_MAPPING = { "-1": "n.a.", "-2": "aufg.",
                                            "-3": "dis." }
                punkte = LEISTUNG_PUNKTE_MAPPING.get("leistung")
            else:
                leistung = float(leistung) / divisor
                if divisor == 1000:
                    leistung = "%.2f" % leistung
                else:
                    leistung = "%.2f" % leistung
                wind = start.serienstart.first().serie.wind
                if wind not in ["", "----"] :
                    leistung += " / %s"  % wind
            leistung = "(%s)" % leistung
            punkte = int(start.serienstart.first().resultat.first().punkte)
            athleten_resultate["punkte_total"] += punkte
            athleten_resultate["disziplinen"][punkteformel] = \
                dict(leistung=leistung, punkte=punkte)
        except AttributeError:
            pass

    rangliste = dict()
    for athlet, item in resultate.iteritems():
        rangliste[item["punkte_total"]] = (athlet, item)

    #import pdb; pdb.set_trace()

    context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                   kategorie_name=kategorie_name, resultate=resultate,
                   rangliste=rangliste)
    return render(request, "meeting/rangliste.html", context)
