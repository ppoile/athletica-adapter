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
