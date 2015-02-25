# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.views import generic
from meeting.models import Meeting


class GruppenEinteilung(generic.View):
    def get(self, request, meeting_id, wettkampf_info, kategorie_name):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        wettkaempfe = meeting.wettkaempfe.filter(
            info=wettkampf_info, kategorie__name=kategorie_name).all()
        import pdb; pdb.set_trace()
        starts = wettkaempfe[0].starts.order_by(
            "anmeldung__athlet__verein__sortierwert",
            "anmeldung__athlet__name",
            "anmeldung__athlet__vorname")

        anmeldungen = []
        for start in starts:
            anmeldungen.append(dict(
                vorname=start.anmeldung.athlet.vorname,
                name=start.anmeldung.athlet.name,
                verein=start.anmeldung.athlet.verein.sortierwert,
                bestleistung=start.anmeldung.bestleistungmk,
                gruppe=start.anmeldung.gruppe))

        context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                       kategorie_name=kategorie_name, anmeldungen=anmeldungen)

        return render(request, "meeting/gruppen-einteilung.html", context)


class SerienEinteilung(generic.View):
    def get(self, request, meeting_id, wettkampf_id):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        wettkampf = meeting.wettkaempfe.get(pk=wettkampf_id)
        starts = wettkampf.starts.order_by("bestleistung")

        anmeldungen = []
        for start in starts:
            anmeldungen.append(dict(
                vorname=start.anmeldung.athlet.vorname,
                name=start.anmeldung.athlet.name,
                verein=start.anmeldung.athlet.verein.sortierwert,
                bestleistung=start.bestleistung,
                gruppe=start.anmeldung.gruppe))

        context = dict(meeting_id=meeting_id, wettkampf_id=wettkampf_id,
                       anmeldungen=anmeldungen)

        return render(request, "meeting/gruppen-einteilung.html", context)
