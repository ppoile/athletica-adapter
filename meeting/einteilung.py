# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.views import generic
from meeting.models import Meeting


class Einteilung(generic.View):
    def get(self, request, meeting_id, wettkampf_info, kategorie_name):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        wettkampf = meeting.wettkaempfe.filter(
            info=wettkampf_info, kategorie__name=kategorie_name).first()
        starts = wettkampf.starts.order_by(
            "anmeldung__athlet__verein__sortierwert",
            "anmeldung__athlet__name",
            "anmeldung__athlet__vorname")

        anmeldungen = []
        for start in starts:
            anmeldungen.append(dict(
                vorname=start.anmeldung.athlet.vorname,
                name=start.anmeldung.athlet.name,
                verein=start.anmeldung.athlet.verein.name,
                bestleistung=start.anmeldung.bestleistungmk,
                gruppe=start.anmeldung.gruppe))

        context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                       kategorie_name=kategorie_name, anmeldungen=anmeldungen)

        return render(request, "meeting/einteilung.html", context)
