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
        for wettkampf in meeting.wettkaempfe.order_by(
                "-kategorie__geschlecht",
                "kategorie__alterslimite",
                "mehrkampfcode",
                "mehrkampfende",
                "mehrkampfreihenfolge",
                "disziplin__name").all():
            kategorie = wettkampf.kategorie.name
            wettkampf_name = wettkampf.info
            match = re.match(r"(\d+K)", wettkampf_name)
            if match:
                wettkampf_name = match.group(0)
            wettkampf_assembler.addDisziplin(kategorie, wettkampf_name,
                                             wettkampf)
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
        context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                       kategorie_name=kategorie_name,
                       wettkampf_name=wettkampf_name, wettkaempfe=wettkaempfe)
        return render(request, "main/wettkampf-detail.html", context)


class WettkampfAssembler(object):
    def __init__(self):
        self._wettkaempfe = OrderedDict()

    def addDisziplin(self, kategorie, wettkampf_name, disziplin):
        try:
            kategorie_wettkaempfe = self._wettkaempfe[kategorie]
        except KeyError:
            kategorie_wettkaempfe = OrderedDict()
            self._wettkaempfe[kategorie] = kategorie_wettkaempfe
        try:
            disziplinen = kategorie_wettkaempfe[wettkampf_name]
        except KeyError:
            disziplinen = list()
            kategorie_wettkaempfe[wettkampf_name] = disziplinen
        disziplinen.append(disziplin)

    def getWettkaempfe(self):
        return self._wettkaempfe
