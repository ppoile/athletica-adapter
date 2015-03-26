# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150303_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rundenset',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AddField(
            model_name='rundenset',
            name='rundenset',
            field=models.IntegerField(default=0, db_column='xRundenset'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='datumvon',
            field=models.DateField(default=datetime.date(2015, 3, 4), db_column='DatumVon'),
        ),
        migrations.AlterField(
            model_name='rundenset',
            name='hauptrunde',
            field=models.IntegerField(default=0, db_column='Hauptrunde', choices=[(1, True), (0, False)]),
        ),
        migrations.AlterField(
            model_name='wettkampf',
            name='typ',
            field=models.IntegerField(db_column='Typ', choices=[(0, 'Einzel'), (1, 'Mehrkampf')]),
        ),
    ]
