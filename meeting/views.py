# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from main.models import Start
from main.models import Wettkampf
from meeting.models import Meeting
from meeting.rangliste import RanglistenItem, Rangliste
from reportlab.pdfgen import canvas


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
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
