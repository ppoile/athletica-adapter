

class RanglistenItem(object):
    _REAL_LEISTUNG_DIVISOR = { "60": 1000, "WEIT": 100, "KUGEL": 100,
                               "HOCH": 100, "600": 1000, "SPEER": 100, "DISKUS": 100, "110H": 1000, "1500": 1000, "STAB": 100, "400": 1000, "100": 1000, }
    _LEISTUNG_MAPPING = { "-1": "n.a.", "-2": "aufg.", "-3": "dis." }

    def __init__(self, name, vorname, jahrgang, verein, land, bem):
        self._name = "%s %s" % (name, vorname)
        self._jahrgang = jahrgang % 100
        self._verein = verein
        self._land = land
        self._bem = bem
        self._disziplinen = dict()
        self._punkte = 0

    def add_disziplin(self, punkteformel, leistung, wind, punkte):
        assert self._disziplinen.get(punkteformel) is None
        self._disziplinen[punkteformel] = dict(leistung=leistung, wind=wind,
                                               punkte=punkte)
        self._punkte += punkte

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

    @property
    def disziplinen_list_text(self):
        disziplinen_texts = []
        for formel, resultat in self._disziplinen.iteritems():
            disziplinen_texts.append(self._get_disziplinen_text(formel, **resultat))
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

    def addStart(self, start):
        athlet = start.anmeldung.athlet
        if athlet.id in self._starts:
            item = self._starts[athlet.id]
        else:
            item = RanglistenItem(athlet.name, athlet.vorname, 2000,
                                  "TV Uster", "SUI", "")
            self._starts[athlet.id] = item

        punkteformel = start.wettkampf.punkteformel
        leistung = start.serienstart.first().resultat.first().leistung
        wind = start.serienstart.first().serie.wind
        punkte = int(start.serienstart.first().resultat.first().punkte)
        item.add_disziplin(punkteformel, leistung, wind, punkte)

    def get_items(self):
        items = list()
        for athlet_id, start in self._starts.iteritems():
            items.append(start)
        return items

    def __unicode__(self):
        return "Hello %s" % self._starts
