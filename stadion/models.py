from django.core.urlresolvers import reverse
from django.db import models

class Stadion(models.Model):
    xstadion = models.IntegerField(db_column='xStadion', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    bahnen = models.IntegerField(db_column='Bahnen')  # Field name made lowercase.
    bahnengerade = models.IntegerField(db_column='BahnenGerade')  # Field name made lowercase.
    ueber1000m = models.CharField(db_column='Ueber1000m', max_length=1, choices=(('y', True), ('n', False)), default='n')  # Field name made lowercase.
    halle = models.CharField(db_column='Halle', max_length=1, choices=(('y', True), ('n', False)), default='n')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stadion:index')

    class Meta:
        managed = False
        db_table = 'stadion'
        verbose_name_plural = "stadien"
