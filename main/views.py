from django.shortcuts import get_object_or_404, render
from main.models import Meeting
from main.models import Stadion

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def sindex(request):
    stadions_list = Stadion.objects.all()
    context = dict(stadions_list=stadions_list)
    return render(request, "main/stadion_index.html", context)

def sdetail(request, stadion_id):
    stadion = get_object_or_404(Stadion, pk=stadion_id)
    anlagen = [item.bezeichnung for item in stadion.anlage_set.all()]
    context = dict(stadion=stadion, anlagen=anlagen)
    return render(request, "main/stadion_details.html", context)

def anmeldungen(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    anmeldungen = [(anmeldung.startnummer,
                    anmeldung.athlet.vorname,
                    anmeldung.athlet.name,
                    anmeldung.athlet.verein.name) for anmeldung in meeting.anmeldungen.all()]
    context = dict(meeting=meeting, anmeldungen=anmeldungen)
    return render(request, "main/anmeldungen.html", context)

[(anmeldung.startnummer,
  anmeldung.athlet.vorname,
  anmeldung.athlet.name,
  anmeldung.athlet.verein.name) for anmeldung in Meeting.objects.first().anmeldungen.filter(athlet__vorname="Cedric")]
