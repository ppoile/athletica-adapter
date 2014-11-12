class RanglistenItem(object):
    _REAL_LEISTUNG_DIVISOR = { "60": 1000, "WEIT": 100, "KUGEL": 100,
                               "HOCH": 100, "600": 1000, "SPEER": 100, "DISKUS": 100, "110H": 1000, "1500": 1000, "STAB": 100, "400": 1000, "100": 1000, }
    _LEISTUNG_MAPPING = { "-1": "n.a.", "-2": "aufg.", "-3": "dis." }

    def __init__(self, name, vorname, jahrgang, verein, land, bem):
        self._name = "%s %s" % (name, vorname)
        self._jahrgang = "%02d" % (jahrgang % 100)
        self._verein = verein
        self._land = land
        self._bem = bem
        self._disziplinen = dict()
        self._punkte = 0

    @property
    def name(self):
        return self._name

    @property
    def jahrgang(self):
        return self._jahrgang

    @property
    def verein(self):
        return self._verein

    @property
    def land(self):
        return self._land

    @property
    def bem(self):
        return self._bem

    @property
    def punkte(self):
        return self._punkte

    def add_disziplin(self, punkteformel, reihenfolge, leistung, wind, punkte):
        assert self._disziplinen.get(punkteformel) is None
        self._disziplinen[(reihenfolge, punkteformel)] = \
            dict(leistung=leistung, wind=wind, punkte=punkte)
        self._punkte += punkte

    @property
    def disziplinen_list_text(self):
        disziplinen_texts = []
        for (reihenfolge, punkteformel), resultat in sorted(self._disziplinen.iteritems()):
            disziplinen_texts.append(self._get_disziplinen_text(punkteformel, **resultat))
        text = ", ".join(disziplinen_texts)
        return text

    def _get_disziplinen_text(self, formel, leistung, wind, punkte):
        text = "%s" % formel
        if leistung in self._LEISTUNG_MAPPING:
            text += " (%s, %s)" % (leistung, self._LEISTUNG_MAPPING[leistung])
            assert punkte == 0
            return text

        divisor = self._REAL_LEISTUNG_DIVISOR[formel]
        leistung = float(leistung) / divisor
        text += " (%.2f" % leistung
        if wind not in ["", "----"] :
            text += " / %s"  % wind
        punkte = int(punkte)
        text += ", %s)"  % punkte
        return text

    def __unicode__(self):
        return "<Hello>"


class Rangliste(object):
    def __init__(self):
        self._starts = dict()

    def add_start(self, start):
        item = self._get_item(start.anmeldung.athlet)
        punkteformel = start.wettkampf.punkteformel
        reihenfolge = start.wettkampf.mehrkampfreihenfolge
        leistung = start.serienstart.first().resultat.first().leistung
        wind = start.serienstart.first().serie.wind
        punkte = int(start.serienstart.first().resultat.first().punkte)
        item.add_disziplin(punkteformel, reihenfolge, leistung, wind, punkte)

    def _get_item(self, athlet):
        """get ranglisten item

        Get existing or new ranglisten item.
        """
        try:
            item = self._starts[athlet.id]
        except KeyError:
            item = RanglistenItem(athlet.name, athlet.vorname, athlet.jahrgang,
                                  athlet.verein, athlet.land, "")
            self._starts[athlet.id] = item
        return item

    def get(self):
        items = list()
        rang = 1
        for athlet_id, start in self._starts.iteritems():
            items.append((rang, start))
            rang += 1
        return items

    def __unicode__(self):
        return "Hello %s" % self._starts
