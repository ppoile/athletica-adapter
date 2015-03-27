# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse
from django.db import models


class Anlage(models.Model):
    id = models.AutoField(db_column='xAnlage', primary_key=True)
    bezeichnung = models.CharField(db_column='Bezeichnung', max_length=20)
    homologiert = models.CharField(db_column='Homologiert', max_length=1,
                                   choices=(('y', 'Yes'), ('n', 'No')),
                                   default='y')
    stadion = models.ForeignKey('Stadion', db_column='xStadion',
                                related_name="anlagen")

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        db_table = 'anlage'
        verbose_name_plural = "anlagen"
        ordering = ["bezeichnung"]


class Anmeldung(models.Model):
    id = models.AutoField(db_column='xAnmeldung', primary_key=True)  # Field name made lowercase.
    startnummer = models.IntegerField(db_column='Startnummer')  # Field name made lowercase.
    erstserie = models.CharField(db_column='Erstserie', max_length=1)  # Field name made lowercase.
    bezahlt = models.CharField(db_column='Bezahlt', max_length=1)  # Field name made lowercase.
    gruppe = models.CharField(db_column='Gruppe', max_length=2)  # Field name made lowercase.
    bestleistungmk = models.FloatField(db_column='BestleistungMK')  # Field name made lowercase.
    vereinsinfo = models.CharField(db_column='Vereinsinfo', max_length=150)  # Field name made lowercase.
    athlet = models.ForeignKey("Athlet", db_column='xAthlet', related_name="anmeldungen")
    meeting = models.ForeignKey("Meeting", db_column='xMeeting', related_name="anmeldungen")
    kategorie = models.ForeignKey("Kategorie", db_column='xKategorie', related_name="-")
    xteam = models.IntegerField(db_column='xTeam')  # Field name made lowercase.
    baseeffortmk = models.CharField(db_column='BaseEffortMK', max_length=1)  # Field name made lowercase.
    anmeldenr_zlv = models.IntegerField(db_column='Anmeldenr_ZLV', blank=True, null=True)  # Field name made lowercase.
    kidid = models.IntegerField(db_column='KidID', blank=True, null=True)  # Field name made lowercase.
    angemeldet = models.CharField(db_column='Angemeldet', max_length=1, blank=True)  # Field name made lowercase.
    vorjahrleistungmk = models.IntegerField(db_column='VorjahrLeistungMK', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return "%s %s" % (self.startnummer, self.athlet)

    class Meta:
        db_table = 'anmeldung'
        verbose_name_plural = "anmeldungen"


class Athlet(models.Model):
    id = models.AutoField(db_column='xAthlet', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    vorname = models.CharField(db_column='Vorname', max_length=50)  # Field name made lowercase.
    jahrgang = models.IntegerField(db_column='Jahrgang', blank=True)  # Field name made lowercase. This field type is a guess.
    verein = models.ForeignKey("Verein", db_column='xVerein', related_name="athleten")
    xverein2 = models.IntegerField(db_column='xVerein2')  # Field name made lowercase.
    lizenznummer = models.IntegerField(db_column='Lizenznummer')  # Field name made lowercase.
    geschlecht = models.CharField(db_column='Geschlecht', max_length=1, choices=(('m', 'Männlich'), ('w', 'Weiblich')))
    land = models.CharField(db_column='Land', max_length=3)  # Field name made lowercase.
    geburtstag = models.DateField(db_column='Geburtstag', blank=True, null=True)
    athleticagen = models.CharField(db_column='Athleticagen', max_length=1)  # Field name made lowercase.
    bezahlt = models.CharField(db_column='Bezahlt', max_length=1)  # Field name made lowercase.
    xregion = models.IntegerField(db_column='xRegion')  # Field name made lowercase.
    lizenztyp = models.IntegerField(db_column='Lizenztyp')  # Field name made lowercase.
    manuell = models.IntegerField(db_column='Manuell')  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=50, blank=True)  # Field name made lowercase.
    plz = models.IntegerField(db_column='Plz', blank=True, null=True)  # Field name made lowercase.
    ort = models.CharField(db_column='Ort', max_length=50, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True)  # Field name made lowercase.

    def __unicode__(self):
        return "%s %s" % (self.vorname, self.name)

    class Meta:
        db_table = 'athlet'
        verbose_name_plural = "athleten"


class BaseAccount(models.Model):
    account_code = models.CharField(max_length=30, primary_key=True)
    account_name = models.CharField(max_length=255)
    account_short = models.CharField(max_length=255)
    account_type = models.CharField(max_length=100)
    lg = models.CharField(max_length=100)

    class Meta:
        db_table = 'base_account'


class BaseAthlete(models.Model):
    id_athlete = models.AutoField(primary_key=True)
    license = models.IntegerField()
    license_paid = models.CharField(max_length=1)
    license_cat = models.CharField(max_length=4)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    nationality = models.CharField(max_length=3)
    account_code = models.CharField(max_length=30)
    second_account_code = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    account_info = models.CharField(max_length=150)

    class Meta:
        db_table = 'base_athlete'


class BaseLog(models.Model):
    id_log = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    update_time = models.DateTimeField()
    global_last_change = models.DateField()

    class Meta:
        db_table = 'base_log'


class BasePerformance(models.Model):
    id_performance = models.AutoField(primary_key=True)
    id_athlete = models.IntegerField()
    discipline = models.IntegerField()
    category = models.CharField(max_length=10)
    best_effort = models.CharField(max_length=15)
    best_effort_date = models.DateField(null=True)
    best_effort_event = models.CharField(max_length=100)
    season_effort = models.CharField(max_length=15)
    season_effort_date = models.DateField(null=True)
    season_effort_event = models.CharField(max_length=100)
    notification_effort = models.CharField(max_length=15)
    notification_effort_date = models.DateField(null=True)
    notification_effort_event = models.CharField(max_length=100)
    season = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_performance'


class BaseRelay(models.Model):
    id_relay = models.AutoField(primary_key=True)
    is_athletica_gen = models.CharField(max_length=1)
    relay_name = models.CharField(max_length=255)
    category = models.CharField(max_length=10)
    discipline = models.CharField(max_length=10)
    account_code = models.IntegerField()

    class Meta:
        db_table = 'base_relay'


class BaseSvm(models.Model):
    id_svm = models.AutoField(primary_key=True)
    is_athletica_gen = models.CharField(max_length=1)
    svm_name = models.CharField(max_length=255)
    svm_category = models.CharField(max_length=10)
    account_code = models.IntegerField()

    class Meta:
        db_table = 'base_svm'


class DisziplinDe(models.Model):
    id = models.AutoField(db_column='xDisziplin', primary_key=True)
    kurzname = models.CharField(db_column='Kurzname', unique=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    anzeige = models.IntegerField(db_column='Anzeige')  # Field name made lowercase.
    seriegroesse = models.IntegerField(db_column='Seriegroesse')  # Field name made lowercase.
    staffellaeufer = models.IntegerField(db_column='Staffellaeufer', blank=True, null=True)  # Field name made lowercase.
    typ = models.IntegerField(db_column='Typ')  # Field name made lowercase.
    appellzeit = models.TimeField(db_column='Appellzeit')  # Field name made lowercase.
    stellzeit = models.TimeField(db_column='Stellzeit')  # Field name made lowercase.
    strecke = models.FloatField(db_column='Strecke')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    xomega_typ = models.IntegerField(db_column='xOMEGA_Typ')  # Field name made lowercase.
    aktiv = models.CharField(max_length=1)

    class Meta:
        db_table = 'disziplin_de'


class DisziplinFr(models.Model):
    id = models.AutoField(db_column='xDisziplin', primary_key=True)
    kurzname = models.CharField(db_column='Kurzname', unique=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    anzeige = models.IntegerField(db_column='Anzeige')  # Field name made lowercase.
    seriegroesse = models.IntegerField(db_column='Seriegroesse')  # Field name made lowercase.
    staffellaeufer = models.IntegerField(db_column='Staffellaeufer', blank=True, null=True)  # Field name made lowercase.
    typ = models.IntegerField(db_column='Typ')  # Field name made lowercase.
    appellzeit = models.TimeField(db_column='Appellzeit')  # Field name made lowercase.
    stellzeit = models.TimeField(db_column='Stellzeit')  # Field name made lowercase.
    strecke = models.FloatField(db_column='Strecke')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    xomega_typ = models.IntegerField(db_column='xOMEGA_Typ')  # Field name made lowercase.
    aktiv = models.CharField(max_length=1)

    class Meta:
        db_table = 'disziplin_fr'


class DisziplinIt(models.Model):
    id = models.AutoField(db_column='xDisziplin', primary_key=True)
    kurzname = models.CharField(db_column='Kurzname', unique=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    anzeige = models.IntegerField(db_column='Anzeige')  # Field name made lowercase.
    seriegroesse = models.IntegerField(db_column='Seriegroesse')  # Field name made lowercase.
    staffellaeufer = models.IntegerField(db_column='Staffellaeufer', blank=True, null=True)  # Field name made lowercase.
    typ = models.IntegerField(db_column='Typ')  # Field name made lowercase.
    appellzeit = models.TimeField(db_column='Appellzeit')  # Field name made lowercase.
    stellzeit = models.TimeField(db_column='Stellzeit')  # Field name made lowercase.
    strecke = models.FloatField(db_column='Strecke')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    xomega_typ = models.IntegerField(db_column='xOMEGA_Typ')  # Field name made lowercase.
    aktiv = models.CharField(max_length=1)

    class Meta:
        db_table = 'disziplin_it'


class Faq(models.Model):
    id = models.AutoField(db_column='xFaq', primary_key=True)
    frage = models.CharField(db_column='Frage', max_length=255)  # Field name made lowercase.
    antwort = models.TextField(db_column='Antwort')  # Field name made lowercase.
    zeigen = models.CharField(db_column='Zeigen', max_length=1)  # Field name made lowercase.
    postop = models.IntegerField(db_column='PosTop')  # Field name made lowercase.
    posleft = models.IntegerField(db_column='PosLeft')  # Field name made lowercase.
    height = models.IntegerField()
    width = models.IntegerField()
    seite = models.CharField(db_column='Seite', max_length=255)  # Field name made lowercase.
    sprache = models.CharField(db_column='Sprache', max_length=2)  # Field name made lowercase.
    farbetitel = models.CharField(db_column='FarbeTitel', max_length=6)  # Field name made lowercase.
    farbehg = models.CharField(db_column='FarbeHG', max_length=6)  # Field name made lowercase.

    class Meta:
        db_table = 'faq'


class Hoehe(models.Model):
    id = models.AutoField(db_column='xHoehe', primary_key=True)
    hoehe = models.IntegerField(db_column='Hoehe')  # Field name made lowercase.
    xrunde = models.IntegerField(db_column='xRunde')  # Field name made lowercase.
    xserie = models.IntegerField(db_column='xSerie')  # Field name made lowercase.

    class Meta:
        db_table = 'hoehe'


class Kategorie(models.Model):
    id = models.AutoField(db_column='xKategorie', primary_key=True)
    kurzname = models.CharField(db_column='Kurzname', unique=True, max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    anzeige = models.IntegerField(db_column='Anzeige')  # Field name made lowercase.
    alterslimite = models.IntegerField(db_column='Alterslimite')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=4)  # Field name made lowercase.
    geschlecht = models.CharField(db_column='Geschlecht', max_length=1)  # Field name made lowercase.
    aktiv = models.CharField(max_length=1)
    ukc = models.CharField(db_column='UKC', max_length=1, blank=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'kategorie'
        verbose_name_plural = "kategorien"


class KategorieSvm(models.Model):
    id = models.AutoField(db_column='xKategorie_svm', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=5)  # Field name made lowercase.

    class Meta:
        db_table = 'kategorie_svm'


class Land(models.Model):
    xcode = models.CharField(db_column='xCode', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    sortierwert = models.IntegerField(db_column='Sortierwert')  # Field name made lowercase.

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'land'
        verbose_name_plural = "länder"


class Layout(models.Model):
    xlayout = models.IntegerField(db_column='xLayout', primary_key=True)  # Field name made lowercase.
    typtl = models.IntegerField(db_column='TypTL')  # Field name made lowercase.
    texttl = models.CharField(db_column='TextTL', max_length=255)  # Field name made lowercase.
    bildtl = models.CharField(db_column='BildTL', max_length=255)  # Field name made lowercase.
    typtc = models.IntegerField(db_column='TypTC')  # Field name made lowercase.
    texttc = models.CharField(db_column='TextTC', max_length=255)  # Field name made lowercase.
    bildtc = models.CharField(db_column='BildTC', max_length=255)  # Field name made lowercase.
    typtr = models.IntegerField(db_column='TypTR')  # Field name made lowercase.
    texttr = models.CharField(db_column='TextTR', max_length=255)  # Field name made lowercase.
    bildtr = models.CharField(db_column='BildTR', max_length=255)  # Field name made lowercase.
    typbl = models.IntegerField(db_column='TypBL')  # Field name made lowercase.
    textbl = models.CharField(db_column='TextBL', max_length=255)  # Field name made lowercase.
    bildbl = models.CharField(db_column='BildBL', max_length=255)  # Field name made lowercase.
    typbc = models.IntegerField(db_column='TypBC')  # Field name made lowercase.
    textbc = models.CharField(db_column='TextBC', max_length=255)  # Field name made lowercase.
    bildbc = models.CharField(db_column='BildBC', max_length=255)  # Field name made lowercase.
    typbr = models.IntegerField(db_column='TypBR')  # Field name made lowercase.
    textbr = models.CharField(db_column='TextBR', max_length=255)  # Field name made lowercase.
    bildbr = models.CharField(db_column='BildBR', max_length=255)  # Field name made lowercase.
    xmeeting = models.IntegerField(db_column='xMeeting')  # Field name made lowercase.

    class Meta:
        db_table = 'layout'


class Meeting(models.Model):
    """
    The meeting class

    # create a meeting
    >>> from main.models import Stadion
    >>> stadion = Stadion.objects.create(name="Buchholz")
    >>> #Meeting.objects.create(name="UMM", stadion=stadion)
    >>> stadion.meetings.create(name="UMM")
    <Meeting: UMM 2015>
    """

    id = models.AutoField(db_column='xMeeting', primary_key=True)
    name = models.CharField(db_column='Name', max_length=60, null=True)
    ort = models.CharField(db_column='Ort', max_length=20)
    datumvon = models.DateField(db_column='DatumVon',
                                default=datetime.date.today())
    datumbis = models.DateField(db_column='DatumBis', blank=True, null=True)
    nummer = models.CharField(db_column='Nummer', max_length=20, default="")
    programmmodus = models.IntegerField(
        db_column='ProgrammModus', choices=(
            (0, "Wettkampfbüro"), (1, "dezentral"),
            (2, "dezentral mit Rangierung")), default=0)
    online = models.CharField(db_column='Online', max_length=1,
                              choices=(('y', True), ('n', False)), default='n')
    organisator = models.CharField(db_column='Organisator', max_length=200)
    zeitmessung = models.CharField(db_column='Zeitmessung', max_length=5)
    passwort = models.CharField(db_column='Passwort', max_length=50)
    stadion = models.ForeignKey("Stadion", db_column='xStadion',
                                related_name="meetings")
    xcontrol = models.IntegerField(db_column='xControl', default=0)
    startgeld = models.FloatField(db_column='Startgeld', default=0)
    startgeldreduktion = models.FloatField(db_column='StartgeldReduktion',
                                           default=0)
    haftgeld = models.FloatField(db_column='Haftgeld', default=0)
    saison = models.CharField(db_column='Saison', max_length=1,
                              choices=(('I', 'Indoor'), ('O', 'Outdoor')), default='O')
    autorangieren = models.CharField(db_column='AutoRangieren', max_length=1)
    UBSKidsCup = models.CharField(db_column='UKC', max_length=1,
                           choices=(('y', True), ('n', False)), default='n')
    statuschanged = models.CharField(db_column='StatusChanged', max_length=1)

    def __str__(self):
        return "%s %d" % (self.name, self.datumvon.year)

    class Meta:
        db_table = 'meeting'


class OmegaTyp(models.Model):
    xomega_typ = models.IntegerField(db_column='xOMEGA_Typ', primary_key=True)  # Field name made lowercase.
    omega_name = models.CharField(db_column='OMEGA_Name', max_length=15)  # Field name made lowercase.
    omega_kurzname = models.CharField(db_column='OMEGA_Kurzname', max_length=4)  # Field name made lowercase.

    class Meta:
        db_table = 'omega_typ'


class Region(models.Model):
    id = models.AutoField(db_column='xRegion', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    anzeige = models.CharField(db_column='Anzeige', max_length=6)  # Field name made lowercase.
    sortierwert = models.IntegerField(db_column='Sortierwert')  # Field name made lowercase.
    ukc = models.CharField(db_column='UKC', max_length=1, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'region'


class Resultat(models.Model):
    id = models.AutoField(db_column='xResultat', primary_key=True)
    leistung = models.IntegerField(db_column='Leistung')  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=5)  # Field name made lowercase.
    punkte = models.FloatField(db_column='Punkte')  # Field name made lowercase.
    serienstart = models.ForeignKey("Serienstart", db_column='xSerienstart', related_name="resultate")

    def __unicode__(self):
        return "%s,%s" % (self.leistung, self.punkte)

    class Meta:
        db_table = 'resultat'
        verbose_name_plural = "resultate"


class Runde(models.Model):
    id = models.AutoField(db_column='xRunde', primary_key=True)
    datum = models.DateField(db_column='Datum')  # Field name made lowercase.
    startzeit = models.TimeField(db_column='Startzeit')  # Field name made lowercase.
    appellzeit = models.TimeField(db_column='Appellzeit')  # Field name made lowercase.
    stellzeit = models.TimeField(db_column='Stellzeit')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    speakerstatus = models.IntegerField(db_column='Speakerstatus')  # Field name made lowercase.
    statuszeitmessung = models.IntegerField(db_column='StatusZeitmessung')  # Field name made lowercase.
    statusupload = models.IntegerField(db_column='StatusUpload')  # Field name made lowercase.
    qualifikationsieger = models.IntegerField(db_column='QualifikationSieger')  # Field name made lowercase.
    qualifikationleistung = models.IntegerField(db_column='QualifikationLeistung')  # Field name made lowercase.
    bahnen = models.IntegerField(db_column='Bahnen')  # Field name made lowercase.
    versuche = models.IntegerField(db_column='Versuche')  # Field name made lowercase.
    gruppe = models.CharField(db_column='Gruppe', max_length=2)  # Field name made lowercase.
    xrundentyp = models.IntegerField(db_column='xRundentyp', blank=True, null=True)  # Field name made lowercase.
    wettkampf = models.ForeignKey("Wettkampf", db_column='xWettkampf', related_name="runden")
    nurbestesresultat = models.CharField(db_column='nurBestesResultat', max_length=1)  # Field name made lowercase.
    statuschanged = models.CharField(db_column='StatusChanged', max_length=1)  # Field name made lowercase.
    endkampf = models.CharField(db_column='Endkampf', max_length=1)  # Field name made lowercase.
    finalisten = models.IntegerField(db_column='Finalisten', blank=True, null=True)  # Field name made lowercase.
    finalnach = models.IntegerField(db_column='FinalNach', blank=True, null=True)  # Field name made lowercase.
    drehen = models.CharField(db_column='Drehen', max_length=20, blank=True)  # Field name made lowercase.
    statusuploadukc = models.IntegerField(db_column='StatusUploadUKC', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        value = "%s" % self.wettkampf
        if self.gruppe:
            value = value[:-1] + ", Gruppe " + self.gruppe + value[-1:]
        return value

    class Meta:
        db_table = 'runde'
        verbose_name_plural = "runden"


class Rundenlog(models.Model):
    id = models.AutoField(db_column='xRundenlog', primary_key=True)
    zeit = models.DateTimeField(db_column='Zeit')  # Field name made lowercase.
    ereignis = models.CharField(db_column='Ereignis', max_length=255)  # Field name made lowercase.
    runde = models.ForeignKey("Runde", db_column='xRunde', related_name="rundenlog")

    class Meta:
        db_table = 'rundenlog'


class Rundenset(models.Model):
    rundenset = models.IntegerField(db_column='xRundenset')
    meeting = models.ForeignKey("Meeting", db_column='xMeeting')
    runde = models.OneToOneField("Runde", db_column='xRunde', related_name="rundenset")
    hauptrunde = models.IntegerField(db_column='Hauptrunde', choices=((1, True), (0, False)), default=0)

    class Meta:
        db_table = 'rundenset'


class RundentypDe(models.Model):
    id = models.AutoField(db_column='xRundentyp', primary_key=True)
    typ = models.CharField(db_column='Typ', unique=True, max_length=2)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.
    wertung = models.IntegerField(db_column='Wertung', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2)  # Field name made lowercase.

    class Meta:
        db_table = 'rundentyp_de'


class RundentypFr(models.Model):
    id = models.AutoField(db_column='xRundentyp', primary_key=True)
    typ = models.CharField(db_column='Typ', unique=True, max_length=2)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.
    wertung = models.IntegerField(db_column='Wertung', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2)  # Field name made lowercase.

    class Meta:
        db_table = 'rundentyp_fr'


class RundentypIt(models.Model):
    id = models.AutoField(db_column='xRundentyp', primary_key=True)
    typ = models.CharField(db_column='Typ', unique=True, max_length=2)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.
    wertung = models.IntegerField(db_column='Wertung', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2)  # Field name made lowercase.

    class Meta:
        db_table = 'rundentyp_it'


class Serie(models.Model):
    id = models.AutoField(db_column='xSerie', primary_key=True)
    bezeichnung = models.CharField(db_column='Bezeichnung', max_length=2)  # Field name made lowercase.
    wind = models.CharField(db_column='Wind', max_length=5, blank=True)  # Field name made lowercase.
    film = models.IntegerField(db_column='Film', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    handgestoppt = models.IntegerField(db_column='Handgestoppt')  # Field name made lowercase.
    runde = models.ForeignKey("Runde", db_column='xRunde', related_name="serien")
    anlage = models.ForeignKey("Anlage", db_column='xAnlage', blank=True, null=True)  # Field name made lowercase.
    tvname = models.CharField(db_column='TVName', max_length=70, blank=True)  # Field name made lowercase.
    maxathlet = models.IntegerField(db_column='MaxAthlet')  # Field name made lowercase.

    def __unicode__(self):
        return "%s (%s)" % (self.bezeichnung, self.runde)

    class Meta:
        db_table = 'serie'
        verbose_name_plural = "serien"


class Serienstart(models.Model):
    id = models.AutoField(db_column='xSerienstart', primary_key=True)
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    bahn = models.IntegerField(db_column='Bahn')  # Field name made lowercase.
    rang = models.IntegerField(db_column='Rang')  # Field name made lowercase.
    qualifikation = models.IntegerField(db_column='Qualifikation')  # Field name made lowercase.
    serie = models.ForeignKey("Serie", db_column='xSerie', related_name="serienstarts")
    start = models.ForeignKey("Start", db_column='xStart', related_name="serienstart")
    rundezusammen = models.IntegerField(db_column='RundeZusammen')  # Field name made lowercase.
    bemerkung = models.CharField(db_column='Bemerkung', max_length=5)  # Field name made lowercase.
    position2 = models.IntegerField(db_column='Position2')  # Field name made lowercase.
    position3 = models.IntegerField(db_column='Position3')  # Field name made lowercase.
    aktivathlet = models.CharField(db_column='AktivAthlet', max_length=1)  # Field name made lowercase.
    starthoehe = models.IntegerField(db_column='Starthoehe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'serienstart'


class Stadion(models.Model):
    id = models.AutoField(db_column='xStadion', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)
    bahnen = models.IntegerField(db_column='Bahnen', default=6)
    bahnengerade = models.IntegerField(db_column='BahnenGerade', default=6)
    ueber1000m = models.CharField(db_column='Ueber1000m', max_length=1,
                                  choices=(('y', True), ('n', False)),
                                  default='n')
    halle = models.CharField(db_column='Halle', max_length=1,
                             choices=(('y', True), ('n', False)), default='n')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stadion:index')

    class Meta:
        db_table = 'stadion'
        verbose_name_plural = "stadien"


class Staffel(models.Model):
    id = models.AutoField(db_column='xStaffel', primary_key=True)
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    xverein = models.IntegerField(db_column='xVerein')  # Field name made lowercase.
    xmeeting = models.IntegerField(db_column='xMeeting')  # Field name made lowercase.
    xkategorie = models.IntegerField(db_column='xKategorie')  # Field name made lowercase.
    xteam = models.IntegerField(db_column='xTeam')  # Field name made lowercase.
    athleticagen = models.CharField(db_column='Athleticagen', max_length=1)  # Field name made lowercase.
    startnummer = models.IntegerField(db_column='Startnummer')  # Field name made lowercase.

    class Meta:
        db_table = 'staffel'


class Staffelathlet(models.Model):
    xstaffelstart = models.IntegerField(db_column='xStaffelstart', primary_key=True)
    xathletenstart = models.IntegerField(db_column='xAthletenstart')  # Field name made lowercase.
    xrunde = models.IntegerField(db_column='xRunde')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        db_table = 'staffelathlet'


class Start(models.Model):
    id = models.AutoField(db_column='xStart', primary_key=True)
    anwesend = models.IntegerField(db_column='Anwesend')  # Field name made lowercase.
    bestleistung = models.IntegerField(db_column='Bestleistung')  # Field name made lowercase.
    bezahlt = models.CharField(db_column='Bezahlt', max_length=1)  # Field name made lowercase.
    erstserie = models.CharField(db_column='Erstserie', max_length=1)  # Field name made lowercase.
    wettkampf = models.ForeignKey("Wettkampf", db_column='xWettkampf', related_name="starts")
    anmeldung = models.ForeignKey("Anmeldung", db_column='xAnmeldung', related_name="starts")
    staffel = models.ForeignKey("Staffel", db_column='xStaffel', blank=True, null=True)
    baseeffort = models.CharField(db_column='BaseEffort', max_length=1)  # Field name made lowercase.
    vorjahrleistung = models.IntegerField(db_column='VorjahrLeistung', blank=True, null=True)  # Field name made lowercase.
    gruppe = models.CharField(db_column='Gruppe', max_length=2, blank=True)  # Field name made lowercase.

    def __unicode__(self):
        return "%s: %s" % (self.anmeldung, self.wettkampf)

    class Meta:
        db_table = 'start'


class Team(models.Model):
    id = models.AutoField(db_column='xTeam', primary_key=True)
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    athleticagen = models.CharField(db_column='Athleticagen', max_length=1)  # Field name made lowercase.
    xkategorie = models.IntegerField(db_column='xKategorie')  # Field name made lowercase.
    xmeeting = models.IntegerField(db_column='xMeeting')  # Field name made lowercase.
    xverein = models.IntegerField(db_column='xVerein')  # Field name made lowercase.
    xkategorie_svm = models.IntegerField(db_column='xKategorie_svm')  # Field name made lowercase.

    class Meta:
        db_table = 'team'


class Teamsm(models.Model):
    id = models.AutoField(db_column='xTeamsm', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    xkategorie = models.IntegerField(db_column='xKategorie')  # Field name made lowercase.
    xverein = models.IntegerField(db_column='xVerein')  # Field name made lowercase.
    xwettkampf = models.IntegerField(db_column='xWettkampf')  # Field name made lowercase.
    xmeeting = models.IntegerField(db_column='xMeeting')  # Field name made lowercase.
    startnummer = models.IntegerField(db_column='Startnummer')  # Field name made lowercase.
    gruppe = models.CharField(db_column='Gruppe', max_length=2, blank=True)  # Field name made lowercase.
    quali = models.IntegerField(db_column='Quali')  # Field name made lowercase.
    leistung = models.IntegerField(db_column='Leistung')  # Field name made lowercase.

    class Meta:
        db_table = 'teamsm'


class Teamsmathlet(models.Model):
    xteamsm = models.IntegerField(db_column='xTeamsm', primary_key=True)
    xanmeldung = models.IntegerField(db_column='xAnmeldung')

    class Meta:
        db_table = 'teamsmathlet'


class Verein(models.Model):
    id = models.AutoField(db_column='xVerein', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100)  # Field name made lowercase.
    sortierwert = models.CharField(db_column='Sortierwert', max_length=100)  # Field name made lowercase.
    xcode = models.CharField(db_column='xCode', max_length=30)  # Field name made lowercase.
    geloescht = models.IntegerField(db_column='Geloescht')  # Field name made lowercase.

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'verein'
        verbose_name_plural = "vereine"

class Videowand(models.Model):
    id = models.AutoField(db_column='xVideowand', primary_key=True)
    xmeeting = models.IntegerField(db_column='xMeeting')  # Field name made lowercase.
    x = models.IntegerField(db_column='X')  # Field name made lowercase.
    y = models.IntegerField(db_column='Y')  # Field name made lowercase.
    inhaltart = models.CharField(db_column='InhaltArt', max_length=4)  # Field name made lowercase.
    inhaltstatisch = models.TextField(db_column='InhaltStatisch')  # Field name made lowercase.
    inhaltdynamisch = models.TextField(db_column='InhaltDynamisch')  # Field name made lowercase.
    aktualisierung = models.IntegerField(db_column='Aktualisierung')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=6)  # Field name made lowercase.
    hintergrund = models.CharField(db_column='Hintergrund', max_length=6)  # Field name made lowercase.
    fordergrund = models.CharField(db_column='Fordergrund', max_length=6)  # Field name made lowercase.
    bildnr = models.IntegerField(db_column='Bildnr')  # Field name made lowercase.

    class Meta:
        db_table = 'videowand'


class Wertungstabelle(models.Model):
    id = models.AutoField(db_column='xWertungstabelle', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'wertungstabelle'


class WertungstabellePunkte(models.Model):
    id = models.AutoField(db_column='xWertungstabelle_Punkte', primary_key=True)
    xwertungstabelle = models.IntegerField(db_column='xWertungstabelle')  # Field name made lowercase.
    xdisziplin = models.IntegerField(db_column='xDisziplin')  # Field name made lowercase.
    geschlecht = models.CharField(db_column='Geschlecht', max_length=1)  # Field name made lowercase.
    leistung = models.CharField(db_column='Leistung', max_length=50)  # Field name made lowercase.
    punkte = models.FloatField(db_column='Punkte')  # Field name made lowercase.

    class Meta:
        db_table = 'wertungstabelle_punkte'


class Wettkampf(models.Model):
    id = models.AutoField(db_column='xWettkampf', primary_key=True)
    TYP_EINZEL = 0
    TYP_MEHRKAMPF = 1
    typ = models.IntegerField(db_column='Typ', choices=((TYP_EINZEL, 'Einzel'),
                                                         (TYP_MEHRKAMPF, 'Mehrkampf')))
    haftgeld = models.FloatField(db_column='Haftgeld')  # Field name made lowercase.
    startgeld = models.FloatField(db_column='Startgeld')  # Field name made lowercase.
    punktetabelle = models.IntegerField(db_column='Punktetabelle')  # Field name made lowercase.
    punkteformel = models.CharField(db_column='Punkteformel', max_length=20)  # Field name made lowercase.
    windmessung = models.IntegerField(db_column='Windmessung')  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=50, blank=True)  # Field name made lowercase.
    zeitmessung = models.IntegerField(db_column='Zeitmessung')  # Field name made lowercase.
    zeitmessungauto = models.IntegerField(db_column='ZeitmessungAuto')  # Field name made lowercase.
    kategorie = models.ForeignKey("Kategorie", db_column='xKategorie')  # Field name made lowercase.
    disziplin = models.ForeignKey("DisziplinDe", db_column='xDisziplin')
    meeting = models.ForeignKey("Meeting", db_column='xMeeting', related_name="wettkaempfe")
    mehrkampfcode = models.IntegerField(db_column='Mehrkampfcode')  # Field name made lowercase.
    mehrkampfende = models.IntegerField(db_column='Mehrkampfende')  # Field name made lowercase.
    mehrkampfreihenfolge = models.IntegerField(db_column='Mehrkampfreihenfolge')  # Field name made lowercase.
    xkategorie_svm = models.IntegerField(db_column='xKategorie_svm')  # Field name made lowercase.
    onlineid = models.IntegerField(db_column='OnlineId')  # Field name made lowercase.
    typaenderung = models.CharField(db_column='TypAenderung', max_length=50)  # Field name made lowercase.

    def __unicode__(self):
        return "%s (%s)" % (self.punkteformel, self.info)

    class Meta:
        db_table = 'wettkampf'
        verbose_name_plural = "wettkämpfe"


class Zeitmessung(models.Model):
    id = models.AutoField(db_column='xZeitmessung', primary_key=True)
    omega_verbindung = models.CharField(db_column='OMEGA_Verbindung', max_length=5)  # Field name made lowercase.
    omega_pfad = models.CharField(db_column='OMEGA_Pfad', max_length=255)  # Field name made lowercase.
    omega_server = models.CharField(db_column='OMEGA_Server', max_length=255)  # Field name made lowercase.
    omega_benutzer = models.CharField(db_column='OMEGA_Benutzer', max_length=50)  # Field name made lowercase.
    omega_passwort = models.CharField(db_column='OMEGA_Passwort', max_length=50)  # Field name made lowercase.
    omega_ftppfad = models.CharField(db_column='OMEGA_Ftppfad', max_length=255)  # Field name made lowercase.
    omega_sponsor = models.CharField(db_column='OMEGA_Sponsor', max_length=255)  # Field name made lowercase.
    alge_typ = models.CharField(db_column='ALGE_Typ', max_length=20)  # Field name made lowercase.
    alge_ftppfad = models.CharField(db_column='ALGE_Ftppfad', max_length=255)  # Field name made lowercase.
    alge_passwort = models.CharField(db_column='ALGE_Passwort', max_length=50)  # Field name made lowercase.
    alge_benutzer = models.CharField(db_column='ALGE_Benutzer', max_length=50)  # Field name made lowercase.
    alge_server = models.CharField(db_column='ALGE_Server', max_length=255)  # Field name made lowercase.
    alge_pfad = models.CharField(db_column='ALGE_Pfad', max_length=255)  # Field name made lowercase.
    alge_verbindung = models.CharField(db_column='ALGE_Verbindung', max_length=5)  # Field name made lowercase.
    xmeeting = models.IntegerField(db_column='xMeeting')  # Field name made lowercase.

    class Meta:
        db_table = 'zeitmessung'
