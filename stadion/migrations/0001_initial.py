# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anlage',
            fields=[
            ],
            options={
                'ordering': ['bezeichnung'],
                'db_table': 'anlage',
                'managed': False,
                'verbose_name_plural': 'anlagen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stadion',
            fields=[
            ],
            options={
                'db_table': 'stadion',
                'managed': False,
                'verbose_name_plural': 'stadien',
            },
            bases=(models.Model,),
        ),
    ]
