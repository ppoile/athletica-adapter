# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.views import generic
from main.models import Meeting
import re


class WettkampfIndex(generic.View):
    def get(self, request, meeting_id):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
        wettkaempfe = list()
        kategorie = None
        mehrkampfcode = None
        for wettkampf in meeting.wettkaempfe.order_by(
                "-kategorie__geschlecht",
                "kategorie__alterslimite",
                "mehrkampfcode",
                "mehrkampfende",
                "mehrkampfreihenfolge",
                "disziplin__name").all():
            if kategorie != wettkampf.kategorie.name:
                kategorie = wettkampf.kategorie.name
                wettkaempfe.append([kategorie, []])
                mehrkampfcode = None
            if mehrkampfcode != wettkampf.mehrkampfcode:
                mehrkampfcode = wettkampf.mehrkampfcode
                wettkampf_name = wettkampf.info
                match = re.match(r"(\d+K)", wettkampf_name)
                if match:
                    wettkampf_name = match.group(0)
                wettkaempfe[-1][1].append([wettkampf_name, []])
            wettkaempfe[-1][-1][-1][1].append(wettkampf)
        context = dict(meeting_id=meeting_id, meeting_name=meeting_name,
                       wettkaempfe=wettkaempfe)
        return render(request, "main/wettkampf-index.html", context)


class WettkampfDetail(generic.View):
    def get(self, request, meeting_id, wettkampf_info, kategorie_name):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        wettkaempfe = meeting.wettkaempfe.filter(
            info=wettkampf_info, kategorie__name=kategorie_name).all()
        context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                       kategorie_name=kategorie_name,wettkaempfe=wettkaempfe)
        return render(request, "main/wettkampf-detail.html", context)
