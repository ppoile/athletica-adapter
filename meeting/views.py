from django.shortcuts import get_object_or_404, render
from django.views import generic
from meeting.models import Meeting

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
