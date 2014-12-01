import math

class Rangliste(object):
    def __init__(self):
        self._items = dict()

    def add_starts(self, starts):
        for start in starts:
            self._add_start(start)

    def _add_start(self, start):
        serienstart = start.serienstart.first()
        if serienstart is None:
            return

        disziplin = start.wettkampf.disziplin.kurzname
        reihenfolge = start.wettkampf.mehrkampfreihenfolge
        windmessung = start.wettkampf.windmessung
        last_disziplin = start.wettkampf.mehrkampfende

        resultate = serienstart.resultat.order_by("-punkte").all()
        for resultat in resultate:
            leistung = resultat.leistung
            wind = ""
            if windmessung:
                wind = serienstart.serie.wind
                if wind == "":
                    wind = resultat.info
            punkte = int(resultat.punkte)
            if not resultat.info.lower().endswith("x"):
                break

        item = self._get_item(start.anmeldung.athlet)
        item.add_disziplin(disziplin, reihenfolge, last_disziplin, leistung,
                           wind, punkte)

    def _get_item(self, athlet):
        """get ranglisten item

        Get existing or new ranglisten item.
        """
        try:
            item = self._items[athlet.id]
        except KeyError:
            item = RanglistenItem(athlet.name, athlet.vorname, athlet.jahrgang,
                                  athlet.verein, athlet.land, "")
            self._items[athlet.id] = item
        return item

    def get(self):
        items = sorted(self._items.values(), reverse=True)
        rangliste = []
        for item in items:
            if item._num_valid_disziplinen() < len(item._disziplinen):
                rang = ""
            elif len(rangliste) > 0 and item == rangliste[-1][1]:
                rang = rangliste[-1][0]
            else:
                rang = "%d." % (len(rangliste) + 1)
            rangliste.append((rang, item))
        return rangliste


class RanglistenItem(object):
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

    def add_disziplin(self, disziplin, reihenfolge, last_disziplin, leistung,
                      wind, punkte):
        assert self._disziplinen.get(disziplin) is None
        self._disziplinen[disziplin] = create_disziplin(
            name=disziplin, reihenfolge=reihenfolge, leistung=leistung,
            wind=wind, punkte=punkte, last_disziplin=last_disziplin)
        self._punkte += punkte

    def disziplinen_list_text(self):
        return ", ".join([str(d) for d in sorted(self._disziplinen.values())])

    def __cmp__(self, other):
        # compare number of completed disziplines
        value = cmp(self._num_valid_disziplinen(),
                    other._num_valid_disziplinen())
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
        for disziplin, resultat in self._disziplinen.iteritems():
            tmp = cmp(resultat.leistung,
                      other._disziplinen[disziplin].leistung)
            if tmp > 0:
                wins += 1
            if tmp < 0:
                other_wins += 1
        value = cmp(wins, other_wins)
        #print "3: cmp(%d, %d) => %d" % (wins, other_wins, value)
        if value != 0:
            return value

        # compare highest punkte
        punkte = [d.punkte for d in self._disziplinen.values()]
        other_punkte = [d.punkte for d in other._disziplinen.values()]
        value = cmp(punkte, other_punkte)
        #print "4: cmp(%s, %s) => %d" % (punkte, other_punkte, value)
        return value

    def _num_valid_disziplinen(self):
        num = 0
        for disziplin in self._disziplinen.values():
            if disziplin.leistung not in [-1, -3]:
                num += 1
        return num


class DisziplinBase(object):
    _LEISTUNG_MAPPING = { -1: "n.a.", -2: "aufg.", -3: "dis." }

    def __init__(self, name, reihenfolge, leistung, wind, punkte,
                 last_disziplin):
        self._name = name
        self._reihenfolge = reihenfolge
        self._leistung = leistung
        if wind not in ["", "----"]:
            wind = wind.rstrip(" m*")
            wind = wind.replace(",", ".")
            wind = float(wind)
        else:
            wind = None
        self._wind = wind
        self._punkte = int(punkte)
        self._last_disziplin = last_disziplin
        assert self._leistung_divisor is not None

    @property
    def name(self):
        return self._name

    @property
    def reihenfolge(self):
        return self._reihenfolge

    @property
    def leistung(self):
        return self._leistung

    @property
    def wind(self):
        return self._wind

    @property
    def punkte(self):
        return self._punkte

    @property
    def last_disziplin(self):
        return self._last_disziplin

    def __str__(self):
        text = "%s" % self.name
        if self.leistung in self._LEISTUNG_MAPPING:
            text += " (%s, %s)" % (self.leistung, self._LEISTUNG_MAPPING[self.leistung])
            assert self.punkte == 0
            return text
        text += " (%s" % self._get_leistung_as_string()
        if self.wind is not None:
            text += " / %.1f"  % self.wind
        text += ", %s)"  % self.punkte
        return text

    def __cmp__(self, other):
        value = cmp(self.last_disziplin, other.last_disziplin)
        if value != 0:
            return value
        value = cmp(self.reihenfolge, other.reihenfolge)
        if value != 0:
            return value
        value = cmp(self.name, other.name)
        if value != 0:
            return value


class MilliSecondsLeistungDisziplin(DisziplinBase):
    _leistung_divisor = 1000

    def _get_leistung_as_string(self):
        hours, rem = divmod(float(self.leistung) / self._leistung_divisor, 3600)
        minutes, seconds = divmod(rem, 60)
        # round to next hundredth of a second
        rounded_seconds = math.ceil(seconds * 100) / 100
        timestring = "%d:%d:%.2f" % (hours, minutes, rounded_seconds)
        timestring = timestring.lstrip("0:")
        #print "hours=%d, minutes=%d, seconds=%.3f => %s" % (
        #    hours, minutes, seconds, timestring)
        return timestring

class CentimeterLeistungDisziplin(DisziplinBase):
    _leistung_divisor = 100

    def _get_leistung_as_string(self):
        return "%.2f" % (float(self.leistung) / self._leistung_divisor)


def create_disziplin(name, reihenfolge, leistung, wind, punkte, last_disziplin):
    if name[0].isdigit():
        disziplin_class = MilliSecondsLeistungDisziplin
    else:
        disziplin_class = CentimeterLeistungDisziplin
    return disziplin_class(name, reihenfolge, leistung, wind, punkte, last_disziplin)
