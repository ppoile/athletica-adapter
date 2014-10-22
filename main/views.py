from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from meeting.models import Meeting

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def anmeldungen(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    anmeldungen = [(anmeldung.startnummer,
                    anmeldung.athlet.vorname,
                    anmeldung.athlet.name,
                    anmeldung.athlet.verein.name) for anmeldung in meeting.anmeldungen.all()]
    context = dict(meeting=meeting, anmeldungen=anmeldungen)
    return render(request, "main/anmeldungen.html", context)
