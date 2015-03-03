# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150303_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlet',
            name='geburtstag',
            field=models.DateField(null=True, db_column='Geburtstag', blank=True),
        ),
    ]
