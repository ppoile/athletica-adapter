# -*- coding: utf-8 -*-

from collections import OrderedDict
from django.shortcuts import get_object_or_404, render
from django.views import generic
from main.models import Meeting
import re


class WettkampfIndex(generic.View):
    def get(self, request, meeting_id):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
        wettkampf_assembler = WettkampfAssembler()
        for kategorie, wettkampf in meeting.wettkaempfe.order_by(
                "-kategorie__geschlecht",
                "kategorie__alterslimite").values_list(
                    "kategorie__name", "info").distinct():
            wettkampf_assembler.addWettkampf(kategorie, wettkampf)
        context = dict(meeting_id=meeting_id, meeting_name=meeting_name,
                       wettkaempfe=wettkampf_assembler.getWettkaempfe())
        return render(request, "main/wettkampf-index.html", context)


class WettkampfDetail(generic.View):
    def get(self, request, meeting_id, wettkampf_info, kategorie_name):
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        wettkaempfe = meeting.wettkaempfe.filter(
            info=wettkampf_info, kategorie__name=kategorie_name).order_by(
                "mehrkampfende",
                "mehrkampfreihenfolge",
                "disziplin__name").all()
        if wettkaempfe.count() > 0:
            wettkampf_name = wettkaempfe.first().info
            match = re.match(r"(\d+K)", wettkampf_name)
            if match:
                wettkampf_name = match.group(0)
        else:
            wettkampf_name = "<no wettkampf>"
        gruppen = wettkaempfe[0].runden.all().values_list("gruppe", flat=True)
        context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                       kategorie_name=kategorie_name,
                       wettkampf_name=wettkampf_name, wettkaempfe=wettkaempfe,
                       gruppen=gruppen)
        return render(request, "main/wettkampf-detail.html", context)


class WettkampfAssembler(object):
    def __init__(self):
        self._wettkaempfe = OrderedDict()

    def addWettkampf(self, kategorie, wettkampf):
        description = wettkampf
        match = re.match(r"(\d+K)", description)
        if match:
            description= match.group(0)
        try:
            wettkaempfe = self._wettkaempfe[kategorie]
        except KeyError:
            wettkaempfe = list()
            self._wettkaempfe[kategorie] = wettkaempfe
        wettkaempfe.append(dict(description=description, info=wettkampf))

    def getWettkaempfe(self):
        return self._wettkaempfe
