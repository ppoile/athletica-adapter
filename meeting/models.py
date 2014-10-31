from django.db import models

class Meeting(models.Model):
    id = models.AutoField(db_column='xMeeting', primary_key=True)
    name = models.CharField(db_column='Name', max_length=60)  # Field name made lowercase.
    ort = models.CharField(db_column='Ort', max_length=20)  # Field name made lowercase.
    datumvon = models.DateField(db_column='DatumVon')  # Field name made lowercase.
    datumbis = models.DateField(db_column='DatumBis', blank=True, null=True)  # Field name made lowercase.
    nummer = models.CharField(db_column='Nummer', max_length=20)  # Field name made lowercase.
    programmmodus = models.IntegerField(db_column='ProgrammModus')  # Field name made lowercase.
    online = models.CharField(db_column='Online', max_length=1)  # Field name made lowercase.
    organisator = models.CharField(db_column='Organisator', max_length=200)  # Field name made lowercase.
    zeitmessung = models.CharField(db_column='Zeitmessung', max_length=5)  # Field name made lowercase.
    passwort = models.CharField(db_column='Passwort', max_length=50)  # Field name made lowercase.
    xstadion = models.IntegerField(db_column='xStadion')  # Field name made lowercase.
    xcontrol = models.IntegerField(db_column='xControl')  # Field name made lowercase.
    startgeld = models.FloatField(db_column='Startgeld')  # Field name made lowercase.
    startgeldreduktion = models.FloatField(db_column='StartgeldReduktion')  # Field name made lowercase.
    haftgeld = models.FloatField(db_column='Haftgeld')  # Field name made lowercase.
    saison = models.CharField(db_column='Saison', max_length=1)  # Field name made lowercase.
    autorangieren = models.CharField(db_column='AutoRangieren', max_length=1)  # Field name made lowercase.
    ukc = models.CharField(db_column='UKC', max_length=1, blank=True)  # Field name made lowercase.
    statuschanged = models.CharField(db_column='StatusChanged', max_length=1)  # Field name made lowercase.

    def __str__(self):
        return "%s %d" % (self.name, self.datumvon.year)

    class Meta:
        managed = False
        db_table = 'meeting'
