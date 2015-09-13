# -*- coding: utf-8 -*-

# fix module search path
import sys
sys.path[0] = '/home/andi/var/athletica-adapter.git'

import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "athletica.settings")

import csv
from django.core.exceptions import ObjectDoesNotExist
from main import models
import operator


class ProcessingError(Exception):
    pass


def getKategorie(event):
    if event == "WOM-10K":
        kategorie = "WOM"
    else:
        kategorie = event.rstrip("*")
        if len(kategorie) > 3:
            kategorie = kategorie[:3] + " " + kategorie[3:]
    try:
        return models.Kategorie.objects.get(name=kategorie)
    except ObjectDoesNotExist:
        raise ProcessingError("kategorie '%s' not found." % kategorie)

def isLicensedEvent(event):
    if event == "WOM-10K":
        return True
    licensed_event = False
    if event.endswith("*"):
        if not (event.startswith("U12") or event.startswith("U14")):
            licensed_event = True
    return licensed_event

def getWettkaempfe(meeting, event):
    kategorien_wettkaempfe = meeting.wettkaempfe.filter(
        kategorie=getKategorie(event))
    if event == "WOM-10K":
        wettkaempfe = kategorien_wettkaempfe.filter(mehrkampfcode=413)
    elif isLicensedEvent(event):
        wettkaempfe = kategorien_wettkaempfe.exclude(
            mehrkampfcode__in=[413, 799])
    else:
        wettkaempfe = kategorien_wettkaempfe.filter(mehrkampfcode=799)
    return wettkaempfe


class Subscription(object):
    _VEREIN_MAPPING = {
        "TV Neue Sektion Winterthur": "TV NS Winterthur",
        "LCR": "LC Regensdorf",
        "TV Kloten-LA": "TV Kloten LA",
        "ATT Adliswil": "Adliswil Track Team",
        "LCZ": u"Leichtathletik Club Zürich",
        u"LC Zürich": u"Leichtathletik Club Zürich",
        "Satus Oerlikon": u"SATUS Zürich-Oerlikon",
        u"LG Küsnacht - Erlenbach": u"LGKE Küsnacht-Erlenbach",
        "BTV Aarau": "BTV Aarau LA",
    }

    _GESCHLECHT_MAPPING = {
        "F": "w",
        "M": "m",
    }

    def __init__(self, data, verbose=False):
        self._data = data
        self._verbose = verbose

    @property
    def data(self):
        return self._data

    def subscribe(self):
        self._meeting = models.Meeting.objects.get(
            name="Uster Mehrkampf Meeting",
            datumvon=datetime.date(2015, 9, 26))
        self._verein = self._get_verein()
        self._athlet = self._get_or_create_athlet()
        self._kategorie = getKategorie(self._data["kategorie"])
        self._anmeldung = self._get_or_create_anmeldung()
        self._wettkaempfe = getWettkaempfe(self._meeting,
                                           self._data["kategorie"])
        self._get_or_create_starts()

    def _get_verein(self):
        verein = self._data["verein"]
        verein = self._VEREIN_MAPPING.get(verein, verein)
        self._data["verein"] = verein
        try:
            return models.Verein.objects.get(name=verein)
        except ObjectDoesNotExist, e:
            import pdb; pdb.set_trace()
            raise ProcessingError("verein '%s' not found" % verein)

    def _get_or_create_athlet(self):
        if self._data["lizenznr"] == "":
            if not self._check_and_update_license_with_unlicensed_athlet():
                return self._get_or_create_unlicensed_athlet()
        return self._get_or_create_licensed_athlet()

    def _check_and_update_license_with_unlicensed_athlet(self):
        arguments = dict(
            firstname=self._data["vorname"],
            lastname=self._data["name"])
        if self._data["jahrgang"] != "":
            arguments.update(birth_date__year=self._data["jahrgang"])
        try:
            base_athlet = models.BaseAthlete.objects.get(**arguments)
            if self._verbose:
                print "Hey, got BaseAthlete (without license): license: %d" % \
base_athlet.license
            self._data["lizenznr"] = base_athlet.license
            return True
        except ObjectDoesNotExist:
            return False

    def _get_or_create_unlicensed_athlet(self):
        geschlecht = self._GESCHLECHT_MAPPING[self._data["mann_frau"].upper()]
        arguments = dict(
            vorname=self._data["vorname"],
            name=self._data["name"],
            jahrgang=self._data["jahrgang"],
            geschlecht=geschlecht,
            verein=self._verein)

        try:
            athlet = models.Athlet.objects.get(**arguments)
            if self._verbose:
                print "got Athlet (without license)"
            return athlet
        except ObjectDoesNotExist:
            athlet = models.Athlet.objects.create(**arguments)
            if self._verbose:
                print "Athlet created (without license)"
            return athlet

    def _get_or_create_licensed_athlet(self):
        base_athlet = self._get_base_athlet()
        athlet = self._get_licensed_athlet()
        if athlet is not None:
            return athlet

        athlet = models.Athlet.objects.create(
            vorname=base_athlet.firstname,
            name=base_athlet.lastname,
            jahrgang=base_athlet.birth_date.year,
            geschlecht=base_athlet.sex,
            lizenznummer=base_athlet.license,
            lizenztyp=models.Athlet.LIZENZTYP_NORMAL_LIZENZ,
            verein=self._verein)
        if self._verbose:
            print "Athlet created (from BaseAthlete)"
        return athlet

    def _get_licensed_athlet(self):
        try:
            athlet = models.Athlet.objects.get(
                lizenznummer=self._data["lizenznr"])
        except ObjectDoesNotExist:
            return None
        if self._verbose:
            print "Got Athlet (with license)"
        self._verify_athlet(athlet)
        return athlet

    def _get_base_athlet(self):
        try:
            base_athlet = models.BaseAthlete.objects.get(
                license=self._data["lizenznr"])
        except ObjectDoesNotExist:
            raise ProcessingError("BaseAthlete: license %s not found" %
                                  self._data["lizenznr"])
        if self._verbose:
            print "Got BaseAthlete"
        self._verify_base_athlet(base_athlet)
        self._check_license_paid(base_athlet)
        return base_athlet

    def _verify_athlet(self, athlet):
        mismatch_items = []
        if athlet.vorname.lower() != self._data["vorname"].lower():
            mismatch_items.append("firstname: %s != %s" % (
                repr(athlet.vorname),  repr(self._data["vorname"])))
        if athlet.name.lower() != self._data["name"].lower():
            mismatch_items.append("lastname: %s != %s" % (
                repr(athlet.name), repr(self._data["name"])))
        if len(mismatch_items) > 0:
            raise ProcessingError(
                "athlet field mismatch (%s)" % ", ".join(mismatch_items))

    def _verify_base_athlet(self, base_athlet):
        mismatch_items = []
        if base_athlet.firstname.lower() != self._data["vorname"].lower():
            mismatch_items.append("firstname: %s != %s" % (
                repr(base_athlet.firstname), repr(self._data["vorname"])))
        if base_athlet.lastname.lower() != self._data["name"].lower():
            mismatch_items.append("lastname: %s != %s" % (
                repr(base_athlet.lastname), repr(self._data["name"])))
        if len(mismatch_items) > 0:
            raise ProcessingError(
                "base_athlet field mismatch (%s)" % ", ".join(mismatch_items))

    def _check_license_paid(self, base_athlet):
        if base_athlet.license_paid == "y":
            return
        if self._verbose:
            print "base_athlet: license not paid!"
        if not self._data["bemerkung"].endswith("(license not paid)"):
            if self._data["bemerkung"] != "":
                self._data["bemerkung"] += " "
            self._data["bemerkung"] += "(license not paid)"

    def _get_or_create_anmeldung(self):
        arguments = dict(
            athlet=self._athlet,
            meeting=self._meeting)
        try:
            anmeldung = self._meeting.anmeldungen.get(**arguments)
            if self._verbose:
                print "got Anmeldung"
            self._update_anmeldung(anmeldung)
            return anmeldung
        except ObjectDoesNotExist:
            arguments.update(dict(
                kategorie=self._kategorie,
                gruppe=self._data["gruppe"]))
            startnummer = self._data["startnummer"]
            if startnummer != "":
                arguments["startnummer"] = startnummer
            anmeldung = models.Anmeldung.objects.create(**arguments)
            if self._verbose:
                print "Anmeldung created"
            return anmeldung

    def _update_anmeldung(self, anmeldung):
        if anmeldung.kategorie != self._kategorie:
            print "anmeldung: updating kategorie: '%s' -> '%s'" % (
                anmeldung.kategorie, self._kategorie)
            anmeldung.kategorie=self._kategorie
            anmeldung.save()
        if anmeldung.gruppe != self._data["gruppe"]:
            print "anmeldung: updating gruppe... '%s' -> '%s'" % (
                anmeldung.gruppe, self._data["gruppe"])
            anmeldung.gruppe=self._data["gruppe"]
            anmeldung.save()
        startnummer = self._data["startnummer"]
        if startnummer == "":
            startnummer = 0
        else:
            startnummer = int(startnummer)
        if anmeldung.startnummer != startnummer:
            print "anmeldung: updating startnummer... %s -> %s" % (
                anmeldung.startnummer, startnummer)
            anmeldung.startnummer=startnummer
            anmeldung.save()

    def _get_or_create_starts(self):
        starts = []
        for wettkampf in self._wettkaempfe:
            arguments = dict(wettkampf=wettkampf,
                             anmeldung=self._anmeldung)
            try:
                start = models.Start.objects.get(**arguments)
                if self._verbose:
                    print "got Start"
            except ObjectDoesNotExist:
                start = models.Start.objects.create(**arguments)
                if self._verbose:
                    print "Start created"
            starts.append(start)
        return starts


class CSV_Processor(object):
    _EXPECTED_HEADINGS = [
        'Verein', 'Lizenznr.', 'Name', 'Vorname', 'Jahrgang', 'Mann/Frau',
        'Kategorie', 'Bemerkung', 'Startnummer', 'Gruppe']

    def __init__(self, verbose):
        self._verbose = verbose

    def process(self, filename):
        def utf8_encoder(value):
            return unicode(value, encoding="utf-8")
        def translate_unicode_to_str(d):
            d2 = dict()
            for k, v in d.iteritems():
                if isinstance(v, unicode):
                    d2[k] = v.encode("utf-8")
                else:
                    d2[k] = v
            return d2
        with open(filename, 'rb') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect=dialect)
            out_filename = filename + ".out"
            with open(out_filename, 'wb+') as csv_outfile:
                headings = self.get_headings(reader, csv_outfile)
                dialect.lineterminator = "\n"
                writer = csv.DictWriter(csv_outfile, fieldnames=headings, dialect=dialect)
                print "processing '%s'..." %  filename
                try:
                    for row in reader:
                        if self._verbose:
                            print ",".join(row)
                        fields = map(utf8_encoder, row)
                        subscription = Subscription(
                            dict(zip(headings, map(unicode.strip, fields))),
                            verbose=self._verbose)
                        subscription.subscribe()
                        writer.writerow(translate_unicode_to_str(
                            subscription.data))
                except ProcessingError, e:
                    print ",".join(row)
                    print unicode(e)
                    sys.exit(1)
    def get_headings(self, reader, outfile):
        def trim_heading(heading):
            return heading.lower().replace(".", "").replace("/", "_")
        headings = None
        while True:
            row = reader.next()
            outfile.write(",".join(row) + "\n")
            if row == self._EXPECTED_HEADINGS:
                return map(trim_heading, row)
        raise ValueError("headings not found")


if __name__ == "__main__":
    import django
    django.setup()

    import argparse
    parser = argparse.ArgumentParser(description='Process subscription.')
    parser.add_argument("files", metavar="<csv-file>", nargs="+",
                        help="file to be parsed")
    parser.add_argument("--delete-objects", "-d", action="store_true",
                        help="delete DB objects beforehand")
    parser.add_argument("--silent", "-s", action="store_true",
                        help="dont be verbose")
    arguments = parser.parse_args()

    if arguments.delete_objects:
        models.Athlet.objects.all().delete()
        models.Anmeldung.objects.all().delete()
        models.Start.objects.all().delete()

    processor = CSV_Processor(verbose=not arguments.silent)
    for filename in arguments.files:
        processor.process(filename)
