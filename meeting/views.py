from django.shortcuts import get_object_or_404, render
from meeting.models import Meeting

def index(request):
    meetings = Meeting.objects.all()
    context = dict(meetings=meetings)
    return render(request, "meeting/index.html", context)

def details(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    context = dict(meeting=meeting)
    return render(request, "meeting/details.html", context)

def anmeldungen(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
    anmeldungen = meeting.anmeldungen.all()
    context = dict(meeting_name=meeting_name, anmeldungen=anmeldungen)
    return render(request, "meeting/anmeldungen.html", context)
