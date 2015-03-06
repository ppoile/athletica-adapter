# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from main.models import Runde
from main.models import Start
from main.models import Wettkampf
from main.models import Meeting
from main.rangliste import RanglistenItem, Rangliste
import os
import re
from webodt.cache import CacheManager
from webodt.helpers import get_mimetype
import webodt.shortcuts


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def anmeldungen(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting_name="%s (%d)" % (meeting.name, meeting.datumvon.year)
    anmeldungen = meeting.anmeldungen.all()
    context = dict(meeting_id=meeting_id, meeting_name=meeting_name,
                   anmeldungen=anmeldungen)
    return render(request, "main/anmeldungen.html", context)


_num_wettkaempfe_info_mapping = {
    4: "Vier",
    5: u"Fünf",
    6: "Sechs",
    7: "Sieben",
    10: "Zehn",
}

def rangliste(request, meeting_id, wettkampf_info, kategorie_name):
    meeting_wettkaempfe = Wettkampf.objects.filter(meeting_id=meeting_id)
    wettkaempfe = meeting_wettkaempfe.filter(
        info=wettkampf_info, kategorie__name=kategorie_name)
    num_wettkaempfe = wettkaempfe.count()
    wettkampf_name = "%s, %skampf" % (
        kategorie_name, _num_wettkaempfe_info_mapping[num_wettkaempfe])

    meeting_starts = Start.objects.filter(wettkampf__meeting_id=meeting_id)
    wettkampf_starts = meeting_starts.filter(
        wettkampf__info=wettkampf_info,
        wettkampf__kategorie__name=kategorie_name)

    rangliste = Rangliste()
    rangliste.add_starts(wettkampf_starts)

    context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                   kategorie_name=kategorie_name,
                   wettkampf_name=wettkampf_name, rangliste=rangliste)
    return render(request, "main/rangliste.html", context)

def rangliste_odt(request, meeting_id, wettkampf_info, kategorie_name):
    meeting_wettkaempfe = Wettkampf.objects.filter(meeting_id=meeting_id)
    wettkaempfe = meeting_wettkaempfe.filter(
        info=wettkampf_info, kategorie__name=kategorie_name)
    num_wettkaempfe = wettkaempfe.count()
    wettkampf_name = "%s, %skampf" % (
        kategorie_name, _num_wettkaempfe_info_mapping[num_wettkaempfe])

    meeting_starts = Start.objects.filter(wettkampf__meeting_id=meeting_id)
    wettkampf_starts = meeting_starts.filter(
        wettkampf__info=wettkampf_info,
        wettkampf__kategorie__name=kategorie_name)
    rangliste = Rangliste()
    rangliste.add_starts(wettkampf_starts)

    context = dict(meeting_id=meeting_id, wettkampf_info=wettkampf_info,
                   kategorie_name=kategorie_name,
                   wettkampf_name=wettkampf_name, rangliste=rangliste)

    return render_to_response(
        template_name='main/rangliste.odt',
        dictionary=context)

def render_to_response(template_name, dictionary=None, context_instance=None,
                       filename=None, format='odt', cache=CacheManager,
                       preprocessors=None, inline=None):
    """
    Using same options as `render_to`, return `django.http.HttpResponse`
    object. The document is automatically removed when the last byte of the
    response is read.
    """
    mimetype = get_mimetype(format)
    content_fd = webodt.shortcuts.render_to(format, template_name, dictionary, context_instance,
        delete_on_close=True, cache=cache, preprocessors=preprocessors
    )
    response = HttpResponse(webodt.shortcuts._ifile(content_fd), content_type=mimetype)
    if not filename:
        filename = os.path.basename(template_name)
    response['Content-Disposition'] = (
        inline and 'inline' or 'attachment; filename="%s"' % filename
    )
    return response
