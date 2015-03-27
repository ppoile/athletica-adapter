# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150326_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='datumvon',
            field=models.DateField(default=datetime.date(2015, 3, 27), db_column='DatumVon'),
        ),
        migrations.AlterField(
            model_name='rundenset',
            name='runde',
            field=models.OneToOneField(related_name='rundenset', db_column='xRunde', to='main.Runde'),
        ),
    ]
