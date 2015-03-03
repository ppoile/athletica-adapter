# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150303_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultat',
            name='serienstart',
            field=models.ForeignKey(related_name='resultate', db_column='xSerienstart', to='main.Serienstart'),
        ),
    ]
