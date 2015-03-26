# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150304_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='anlage',
            field=models.ForeignKey(db_column='xAnlage', blank=True, to='main.Anlage', null=True),
        ),
        migrations.AlterField(
            model_name='start',
            name='staffel',
            field=models.ForeignKey(db_column='xStaffel', blank=True, to='main.Staffel', null=True),
        ),
    ]
