# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Anlage',
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.DeleteModel(
            name='Stadion',
        ),
        migrations.AlterModelOptions(
            name='anmeldung',
            options={'verbose_name_plural': 'anmeldungen'},
        ),
        migrations.AlterModelOptions(
            name='athlet',
            options={'verbose_name_plural': 'athleten'},
        ),
        migrations.AlterModelOptions(
            name='kategorie',
            options={'verbose_name_plural': 'kategorien'},
        ),
        migrations.AlterModelOptions(
            name='land',
            options={'verbose_name_plural': 'l\xe4nder'},
        ),
        migrations.AlterModelOptions(
            name='resultat',
            options={'verbose_name_plural': 'resultate'},
        ),
        migrations.AlterModelOptions(
            name='runde',
            options={'verbose_name_plural': 'runden'},
        ),
        migrations.AlterModelOptions(
            name='serie',
            options={'verbose_name_plural': 'serien'},
        ),
        migrations.AlterModelOptions(
            name='verein',
            options={'verbose_name_plural': 'vereine'},
        ),
        migrations.AlterModelOptions(
            name='wettkampf',
            options={'verbose_name_plural': 'wettk\xe4mpfe'},
        ),
    ]
