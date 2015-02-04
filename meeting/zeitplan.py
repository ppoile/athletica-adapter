from django.shortcuts import get_object_or_404, render
from django.views import generic
from main.models import Runde
from meeting.models import Meeting
from operator import attrgetter
import re


class Zeitplan(generic.View):
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
                               info=self._get_info(runde)))
            kategorien.add(kategorie)
        kategorien_labels = self._get_sorted_kategorien_labels(kategorien)

        # assemble table data
        headings = ["Zeit"] + kategorien_labels
        data = []
        datum = None
        for runde in runden:
            if datum != runde["datum"]:
                datum = runde["datum"]
                data.append([datum])
            row = [runde["zeit"]]
            index = kategorien_labels.index(runde["kategorie"])
            for i in range(index):
                row.append("-")
            row.append(runde["info"])
            for i in range(len(headings) - len(row)):
                row.append("-")
            data.append(row)

        context = dict(meeting_id=meeting_id,
                       meeting_name=meeting_name,
                       headings = headings,
                       data=data)
        return render(request, "meeting/zeitplan.html", context)

    def _get_sorted_kategorien_labels(self, kategorien):
        sorted_kategorien = sorted(
            kategorien, key=attrgetter("geschlecht", "alterslimite"),
            reverse=True)
        return [k.name for k in sorted_kategorien]

    def _get_info(self, runde):
        info = runde.wettkampf.punkteformel
        if info[0].isalpha():
            info = info.capitalize()
        gruppe = runde.wettkampf.info
        match = re.match(r"(\d+K)", runde.wettkampf.info)
        if match:
            gruppe = match.group(0)
        if runde.gruppe:
            gruppe += " G%s" % runde.gruppe
        info += " (%s)" % gruppe
        return info
