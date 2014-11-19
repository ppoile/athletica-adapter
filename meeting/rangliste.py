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

    def __cmp__(self, other):
        # compare number of completed disziplines
        value = cmp(self._num_valid_disziplinen(), other._num_valid_disziplinen())
        #print "1: cmp(%d, %d) => %d" % (self._num_valid_disziplinen(),
        #                                other._num_valid_disziplinen(), value)
        if value != 0:
            return value

        # compare punkte
        value = cmp(self.punkte, other.punkte)
        #print "2: cmp(%d, %d) => %d" % (self.punkte, other.punkte, value)
        if value != 0:
            return value

        # compare diszipline wins
        wins = 0
        other_wins = 0
        for reihenfolge_disziplin, resultat in self._disziplinen.iteritems():
            tmp = cmp(resultat["leistung"], other._disziplinen[reihenfolge_disziplin]["leistung"])
            if tmp > 0:
                wins += 1
            if tmp < 0:
                other_wins += 1
        value = cmp(wins, other_wins)
        #print "3: cmp(%d, %d) => %d" % (wins, other_wins, value)
        if value != 0:
            return value

        # compare highest punkte
        punkte = [item["punkte"] for item in self._disziplinen.values()]
        other_punkte = [item["punkte"] for item in other._disziplinen.values()]
        value = cmp(punkte, other_punkte)
        #print "4: cmp(%s, %s) => %d" % (punkte, other_punkte, value)
        return value

    def _num_valid_disziplinen(self):
        num = 0
        for disziplin in self._disziplinen.values():
            if disziplin["leistung"] not in [-1, -3]:
                num += 1
        return num


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
        items = sorted(self._starts.values(), reverse=True)
        rangliste = []
        for item in items:
            if len(rangliste) > 0 and item == rangliste[-1][1]:
                rang = rangliste[-1][0]
            else:
                rang = len(rangliste) + 1
            rangliste.append((rang, item))
        return rangliste
