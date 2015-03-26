# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_squashed_0005_auto_20150304_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rundenset',
            name='rundenset',
            field=models.IntegerField(db_column='xRundenset'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='anlage',
            field=models.ForeignKey(to='main.Anlage', db_column='xAnlage'),
        ),
        migrations.AlterField(
            model_name='start',
            name='staffel',
            field=models.ForeignKey(to='main.Staffel', db_column='xStaffel'),
        ),
    ]
