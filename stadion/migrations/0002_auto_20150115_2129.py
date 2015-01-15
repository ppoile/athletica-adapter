# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stadion', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Anlage',
        ),
        migrations.CreateModel(
            name='Anlage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'xAnlage')),
                ('bezeichnung', models.CharField(max_length=20, db_column=b'Bezeichnung')),
                ('homologiert', models.CharField(default=b'y', max_length=1, db_column=b'Homologiert', choices=[(b'y', b'Yes'), (b'n', b'No')])),
            ],
            options={
                'ordering': ['bezeichnung'],
                'db_table': 'anlage',
                'verbose_name_plural': 'anlagen',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Stadion',
        ),
        migrations.CreateModel(
            name='Stadion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'xStadion')),
                ('name', models.CharField(max_length=50, db_column=b'Name')),
                ('bahnen', models.IntegerField(db_column=b'Bahnen')),
                ('bahnengerade', models.IntegerField(db_column=b'BahnenGerade')),
                ('ueber1000m', models.CharField(default=b'n', max_length=1, db_column=b'Ueber1000m', choices=[(b'y', True), (b'n', False)])),
                ('halle', models.CharField(default=b'n', max_length=1, db_column=b'Halle', choices=[(b'y', True), (b'n', False)])),
            ],
            options={
                'db_table': 'stadion',
                'verbose_name_plural': 'stadien',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='anlage',
            name='stadion',
            field=models.ForeignKey(related_name=b'anlagen', db_column=b'xStadion', to='stadion.Stadion'),
            preserve_default=True,
        ),
    ]
