# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from main.models import Start
from main.models import Wettkampf
from meeting.models import Meeting
from meeting.rangliste import RanglistenItem, Rangliste
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer


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
    meeting_wettkaempfe = Wettkampf.objects.filter(meeting_id=meeting_id)
    wettkaempfe = meeting_wettkaempfe.filter(
        info=wettkampf_info, kategorie__name=kategorie_name)
    num_wettkaempfe = wettkaempfe.count()
    num_wettkaempfe_info_mapping = {
        4: "Vier",
        5: u"Fünf",
        6: "Sechs",
        7: "Sieben",
        10: "Zehn",
    }
    wettkampf_name = "%s, %skampf" % (
        kategorie_name, num_wettkaempfe_info_mapping[num_wettkaempfe])

    meeting_starts = Start.objects.filter(wettkampf__meeting_id=meeting_id)
    starts = meeting_starts.filter(wettkampf__info=wettkampf_info,
                                   wettkampf__kategorie__name=kategorie_name)
    ordered_starts = starts.order_by("anmeldung__athlet")
    rangliste = Rangliste()
    for start in ordered_starts:
        rangliste.add_start(start)

    context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                   kategorie_name=kategorie_name,
                   wettkampf_name=wettkampf_name,
                   rangliste=rangliste)
    return render(request, "meeting/rangliste.html", context)

def rangliste_pdf(request, meeting_id, wettkampf_info, kategorie_name):
    meeting_wettkaempfe = Wettkampf.objects.filter(meeting_id=meeting_id)
    wettkaempfe = meeting_wettkaempfe.filter(
        info=wettkampf_info, kategorie__name=kategorie_name)
    num_wettkaempfe = wettkaempfe.count()
    num_wettkaempfe_info_mapping = {
        4: "Vier",
        5: u"Fünf",
        6: "Sechs",
        7: "Sieben",
        10: "Zehn",
    }
    wettkampf_name = "%s, %skampf" % (
        kategorie_name, num_wettkaempfe_info_mapping[num_wettkaempfe])

    meeting_starts = Start.objects.filter(wettkampf__meeting_id=meeting_id)
    starts = meeting_starts.filter(wettkampf__info=wettkampf_info,
                                   wettkampf__kategorie__name=kategorie_name)
    ordered_starts = starts.order_by("anmeldung__athlet")
    rangliste = Rangliste()
    for start in ordered_starts:
        rangliste.add_start(start)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rangliste.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)

    elements = []
    styles=getSampleStyleSheet()
    styleN = styles["Normal"]

    headings = ["Rang", "Name", "Jg", "Verein", "Land", "Punkte", "Bem"]
    data = [headings]
    for rang, start in rangliste.get():
        data.append([rang, start.name, start.jahrgang, start.verein,
                     start.land, start.punkte, start.bem])
                     #start.disziplinen_list_text])

    tableThatSplitsOverPages = Table(data, [2.5 * cm, 2.5 * cm], repeatRows=1)
    elements.append(tableThatSplitsOverPages)

    doc.build(elements)

    return response
