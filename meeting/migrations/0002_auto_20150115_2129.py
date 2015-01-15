# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stadion', '0002_auto_20150115_2129'),
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'xMeeting')),
                ('name', models.CharField(max_length=60, db_column=b'Name')),
                ('ort', models.CharField(max_length=20, db_column=b'Ort')),
                ('datumvon', models.DateField(db_column=b'DatumVon')),
                ('datumbis', models.DateField(null=True, db_column=b'DatumBis', blank=True)),
                ('nummer', models.CharField(max_length=20, db_column=b'Nummer')),
                ('programmmodus', models.IntegerField(db_column=b'ProgrammModus')),
                ('online', models.CharField(max_length=1, db_column=b'Online')),
                ('organisator', models.CharField(max_length=200, db_column=b'Organisator')),
                ('zeitmessung', models.CharField(max_length=5, db_column=b'Zeitmessung')),
                ('passwort', models.CharField(max_length=50, db_column=b'Passwort')),
                ('xcontrol', models.IntegerField(db_column=b'xControl')),
                ('startgeld', models.FloatField(db_column=b'Startgeld')),
                ('startgeldreduktion', models.FloatField(db_column=b'StartgeldReduktion')),
                ('haftgeld', models.FloatField(db_column=b'Haftgeld')),
                ('saison', models.CharField(max_length=1, db_column=b'Saison')),
                ('autorangieren', models.CharField(max_length=1, db_column=b'AutoRangieren')),
                ('ukc', models.CharField(max_length=1, db_column=b'UKC', blank=True)),
                ('statuschanged', models.CharField(max_length=1, db_column=b'StatusChanged')),
                ('stadion', models.ForeignKey(related_name=b'meetings', db_column=b'xStadion', to='stadion.Stadion')),
            ],
            options={
                'db_table': 'meeting',
            },
            bases=(models.Model,),
        ),
    ]
