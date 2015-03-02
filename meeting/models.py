# -*- coding: utf-8 -*-

import datetime
from django.db import models

class Meeting(models.Model):
    """
    The meeting class

    # create a meeting
    >>> from stadion.models import Stadion
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
    stadion = models.ForeignKey("stadion.Stadion", db_column='xStadion',
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
