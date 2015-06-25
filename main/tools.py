# -*- coding: utf-8 -*-

# fix module search path
import sys
sys.path[0] = '/home/andi/var/athletica-adapter.git'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "athletica.settings")

import csv
from django.core.exceptions import ObjectDoesNotExist
from main import models
import operator


def getWettkaempfe(meeting, event):
    licensed_event = False
    if event.endswith("*"):
        if not (event.startswith("U12") or event.startswith("U14")):
            licensed_event = True
    kategorie = event.rstrip("*")
    if len(kategorie) > 3:
        kategorie = kategorie[:3] + " " + kategorie[3:]
    kategorien_wettkaempfe = meeting.wettkaempfe.filter(
        kategorie__name=kategorie)
    if licensed_event:
        wettkaempfe = kategorien_wettkaempfe.exclude(
            mehrkampfcode=799)
    else:
        wettkaempfe = kategorien_wettkaempfe.filter(
            mehrkampfcode=799)
    return wettkaempfe

class Subscription(object):
    _VEREIN_MAPPING = {
        "TV Neue Sektion Winterthur": "TV NS Winterthur",
        "LCR": "LC Regensdorf",
        "TV Kloten - LA": "TV Kloten LA",
        "ATT Adliswil": "Adliswil Track Team",
        "LCZ": u"LC Zürich",
        "Satus Oerlikon": u"SATUS Zürich-Oerlikon",
        u"LG Küsnacht - Erlenbach": u"LG Küsnacht-Erlenbach",
    }

    _GESCHLECHT_MAPPING = {
        "F": "w",
        "M": "m",
    }

    def __init__(self, data):
        self._data = data

    def subscribe(self):
        verein = self._get_verein()
        return self._get_or_create_athlet(verein)

    def _get_verein(self):
        name = self._data["verein"]
        name = self._VEREIN_MAPPING.get(name, name)
        try:
            return models.Verein.objects.get(name=name)
        except ObjectDoesNotExist, e:
            print "verein '%s' not found." % name
            import pdb; pdb.set_trace()
            raise

    def _get_or_create_athlet(self, verein):
        lizenz = self._data["lizenznr"]
        if lizenz != "":
            try:
                athlet = models.Athlet.objects.get(lizenznummer=lizenz)
                print "got Athlet (with license)"
                if athlet.name != self._data["name"] or athlet.vorname != self._data["vorname"]:
                    import pdb; pdb.set_trace()
                return athlet
            except ObjectDoesNotExist, e:
                pass

            try:
                base_athlete = models.BaseAthlete.objects.get(
                    license=self._data["lizenznr"])
                #print "got BaseAthlete (with license)"
            except ObjectDoesNotExist, e:
                print "BaseAthlete not found."
                import pdb; pdb.set_trace()
                raise

            if base_athlete.firstname.lower() != self._data["vorname"].lower():
                report = "%s != %s" % (repr(base_athlete.firstname),
                                       repr(self._data["vorname"]))
                print report
                import pdb; pdb.set_trace()
            if base_athlete.lastname.lower() != self._data["name"].lower():
                report = "%s != %s" % (repr(base_athlete.lastname),
                                       repr(self._data["name"]))
                print report
                import pdb; pdb.set_trace()

            args = dict(
                vorname=base_athlete.firstname,
                name=base_athlete.lastname,
                jahrgang=base_athlete.birth_date.year,
                geschlecht=base_athlete.sex,
                lizenznummer=base_athlete.license,
                verein=verein,
            )
            athlet = models.Athlet.objects.create(**args)
            print "Athlet created (from BaseAthlete)"
            return athlet
        else:
            geschlecht = self._GESCHLECHT_MAPPING[self._data["mann_frau"]]
            args = dict(
                vorname=self._data["vorname"],
                name=self._data["name"],
                jahrgang=self._data["jahrgang"],
                geschlecht=geschlecht,
                verein=verein,
            )
    
            try:
                athlet = models.Athlet.objects.get(**args)
                print "got Athlet (without license)"
                return athlet
            except ObjectDoesNotExist, e:
                athlet = models.Athlet.objects.create(**args)
                print "Athlet created (without license)"
                return athlet


class CSV_Processor(object):
    _EXPECTED_HEADINGS = [
        'Verein', 'Lizenznr.', 'Name', 'Vorname', 'Jahrgang', 'Mann/Frau',
        'Kategorie', 'Bemerkung', 'Startnummer', 'Gruppe']

    def get_headings(self, reader):
        def trim_heading(heading):
            return heading.lower().replace(".", "").replace("/", "_")
        headings = None
        while True:
            row = reader.next()
            if row == self._EXPECTED_HEADINGS:
                return map(trim_heading, row)
        raise ValueError("headings not found")

    def process(self, filename):
        def utf8_encoder(value):
            return unicode(value, encoding="utf-8")
        with open(filename, 'rb') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            headings = self.get_headings(reader)
            #print "headings: %s" % headings
            for row in reader:
                #print repr(",".join(row))
                fields = map(utf8_encoder, row)
                #print repr(fields)
                subscription = Subscription(dict(zip(headings, fields)))
                athlet = subscription.subscribe()


if __name__ == "__main__":
    import django
    django.setup()

    import argparse
    parser = argparse.ArgumentParser(description='Process subscription.')
    parser.add_argument("files", metavar="<csv-file>", nargs="+", help="file to be parsed")
    args = parser.parse_args()
    processor = CSV_Processor()
    for filename in args.files:
        processor.process(filename)
