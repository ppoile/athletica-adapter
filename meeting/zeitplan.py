from django.shortcuts import get_object_or_404, render
from django.views import generic
from main.models import Runde
from meeting.models import Meeting
from operator import attrgetter


class Zeitplan(generic.View):
    def _get_sorted_kategorien_labels(self, kategorien):
        sorted_kategorien = sorted(
            kategorien, key=attrgetter("geschlecht", "alterslimite"),
            reverse=True)
        return [k.name for k in sorted_kategorien]

    def get(self, request, meeting_id):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
        meeting_runden = Runde.objects.filter(
            wettkampf__meeting_id=meeting_id).order_by("datum", "stellzeit").all()
        runden = list()
        kategorien = set()
        for runde in meeting_runden:
            kategorie = runde.wettkampf.kategorie
            runden.append(dict(datum=runde.datum,
                               zeit=runde.startzeit,
                               kategorie=kategorie.name,
                               gruppe=runde.gruppe,
                               disziplin=runde.wettkampf.punkteformel))
            kategorien.add(kategorie)
        kategorien_labels = self._get_sorted_kategorien_labels(kategorien)
        context = dict(meeting_id=meeting_id,
                       meeting_name=meeting_name,
                       runden=runden,
                       kategorien=kategorien_labels)
        return render(request, "meeting/zeitplan.html", context)
