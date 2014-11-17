class RanglistenItem(object):
    def _get_leistung_divisor(self, disziplin):
        if disziplin[0].isdigit():
            return 1000
        return 100

    _LEISTUNG_MAPPING = { -1: "n.a.", -2: "aufg.", -3: "dis." }

    def __init__(self, name, vorname, jahrgang, verein, land, bem):
        self._name = "%s %s" % (name, vorname)
        self._jahrgang = "%02d" % (jahrgang % 100)
        self._verein = verein
        if land == "-":
            land = ""
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

    def add_disziplin(self, disziplin, reihenfolge, leistung, wind, punkte):
        assert self._disziplinen.get(disziplin) is None
        self._disziplinen[(reihenfolge, disziplin)] = \
            dict(leistung=leistung, wind=wind, punkte=punkte)
        self._punkte += punkte

    @property
    def disziplinen_list_text(self):
        disziplinen_texts = []
        for (reihenfolge, disziplin), resultat in sorted(self._disziplinen.iteritems()):
            disziplinen_texts.append(self._get_disziplinen_text(disziplin, **resultat))
        text = ", ".join(disziplinen_texts)
        return text

    def _get_disziplinen_text(self, disziplin, leistung, wind, punkte):
        text = "%s" % disziplin
        if leistung in self._LEISTUNG_MAPPING:
            text += " (%s, %s)" % (leistung, self._LEISTUNG_MAPPING[leistung])
            assert punkte == 0
            return text

        divisor = self._get_leistung_divisor(disziplin)
        leistung = float(leistung) / divisor
        text += " (%.2f" % leistung
        if wind not in ["", "----"] :
            wind = wind.rstrip(" m")
            wind = wind.replace(",", ".")
            wind = float(wind)
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
        disziplin = start.wettkampf.disziplin.kurzname
        reihenfolge = start.wettkampf.mehrkampfreihenfolge
        serienstart = start.serienstart.first()
        if serienstart is None:
            return

        resultate = serienstart.resultat.order_by("-punkte").all()
        for resultat in resultate:
            leistung = resultat.leistung
            wind = serienstart.serie.wind
            punkte = int(resultat.punkte)
            if not resultat.info.lower().endswith("x"):
                break

        item = self._get_item(start.anmeldung.athlet)
        item.add_disziplin(disziplin, reihenfolge, leistung, wind, punkte)

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
        items = dict()
        for athlet_id, start in self._starts.iteritems():
            try:
                item = items[start.punkte]
            except KeyError:
                item = []
                items[start.punkte] = item
            item.append(start)

        rangliste = []
        rang = 1
        for punkte, starts in sorted(items.iteritems(), reverse=True):
            for start in starts:
                rangliste.append((rang, start))
            rang += len(starts)
        return rangliste

    def __unicode__(self):
        return "Hello %s" % self._starts
