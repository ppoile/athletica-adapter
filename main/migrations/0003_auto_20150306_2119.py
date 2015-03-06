# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141105_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anlage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xAnlage')),
                ('bezeichnung', models.CharField(max_length=20, db_column='Bezeichnung')),
                ('homologiert', models.CharField(default='y', max_length=1, db_column='Homologiert', choices=[('y', 'Yes'), ('n', 'No')])),
            ],
            options={
                'ordering': ['bezeichnung'],
                'db_table': 'anlage',
                'verbose_name_plural': 'anlagen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xMeeting')),
                ('name', models.CharField(max_length=60, null=True, db_column='Name')),
                ('ort', models.CharField(max_length=20, db_column='Ort')),
                ('datumvon', models.DateField(default=datetime.date(2015, 3, 6), db_column='DatumVon')),
                ('datumbis', models.DateField(null=True, db_column='DatumBis', blank=True)),
                ('nummer', models.CharField(default='', max_length=20, db_column='Nummer')),
                ('programmmodus', models.IntegerField(default=0, db_column='ProgrammModus', choices=[(0, 'Wettkampfb\xfcro'), (1, 'dezentral'), (2, 'dezentral mit Rangierung')])),
                ('online', models.CharField(default='n', max_length=1, db_column='Online', choices=[('y', True), ('n', False)])),
                ('organisator', models.CharField(max_length=200, db_column='Organisator')),
                ('zeitmessung', models.CharField(max_length=5, db_column='Zeitmessung')),
                ('passwort', models.CharField(max_length=50, db_column='Passwort')),
                ('xcontrol', models.IntegerField(default=0, db_column='xControl')),
                ('startgeld', models.FloatField(default=0, db_column='Startgeld')),
                ('startgeldreduktion', models.FloatField(default=0, db_column='StartgeldReduktion')),
                ('haftgeld', models.FloatField(default=0, db_column='Haftgeld')),
                ('saison', models.CharField(default='O', max_length=1, db_column='Saison', choices=[('I', 'Indoor'), ('O', 'Outdoor')])),
                ('autorangieren', models.CharField(max_length=1, db_column='AutoRangieren')),
                ('UBSKidsCup', models.CharField(default='n', max_length=1, db_column='UKC', choices=[('y', True), ('n', False)])),
                ('statuschanged', models.CharField(max_length=1, db_column='StatusChanged')),
            ],
            options={
                'db_table': 'meeting',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stadion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xStadion')),
                ('name', models.CharField(max_length=50, db_column='Name')),
                ('bahnen', models.IntegerField(default=6, db_column='Bahnen')),
                ('bahnengerade', models.IntegerField(default=6, db_column='BahnenGerade')),
                ('ueber1000m', models.CharField(default='n', max_length=1, db_column='Ueber1000m', choices=[('y', True), ('n', False)])),
                ('halle', models.CharField(default='n', max_length=1, db_column='Halle', choices=[('y', True), ('n', False)])),
            ],
            options={
                'db_table': 'stadion',
                'verbose_name_plural': 'stadien',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meeting',
            name='stadion',
            field=models.ForeignKey(related_name='meetings', db_column='xStadion', to='main.Stadion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='anlage',
            name='stadion',
            field=models.ForeignKey(related_name='anlagen', db_column='xStadion', to='main.Stadion'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Anmeldung',
        ),
        migrations.CreateModel(
            name='Anmeldung',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xAnmeldung')),
                ('startnummer', models.IntegerField(db_column='Startnummer')),
                ('erstserie', models.CharField(max_length=1, db_column='Erstserie')),
                ('bezahlt', models.CharField(max_length=1, db_column='Bezahlt')),
                ('gruppe', models.CharField(max_length=2, db_column='Gruppe')),
                ('bestleistungmk', models.FloatField(db_column='BestleistungMK')),
                ('vereinsinfo', models.CharField(max_length=150, db_column='Vereinsinfo')),
                ('xteam', models.IntegerField(db_column='xTeam')),
                ('baseeffortmk', models.CharField(max_length=1, db_column='BaseEffortMK')),
                ('anmeldenr_zlv', models.IntegerField(null=True, db_column='Anmeldenr_ZLV', blank=True)),
                ('kidid', models.IntegerField(null=True, db_column='KidID', blank=True)),
                ('angemeldet', models.CharField(max_length=1, db_column='Angemeldet', blank=True)),
                ('vorjahrleistungmk', models.IntegerField(null=True, db_column='VorjahrLeistungMK', blank=True)),
                ('meeting', models.ForeignKey(related_name='anmeldungen', db_column='xMeeting', to='main.Meeting')),
            ],
            options={
                'db_table': 'anmeldung',
                'verbose_name_plural': 'anmeldungen',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Athlet',
        ),
        migrations.CreateModel(
            name='Athlet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xAthlet')),
                ('name', models.CharField(max_length=50, db_column='Name')),
                ('vorname', models.CharField(max_length=50, db_column='Vorname')),
                ('jahrgang', models.IntegerField(db_column='Jahrgang', blank=True)),
                ('xverein2', models.IntegerField(db_column='xVerein2')),
                ('lizenznummer', models.IntegerField(db_column='Lizenznummer')),
                ('geschlecht', models.CharField(max_length=1, db_column='Geschlecht', choices=[('m', 'M\xe4nnlich'), ('w', 'Weiblich')])),
                ('land', models.CharField(max_length=3, db_column='Land')),
                ('geburtstag', models.DateField(db_column='Geburtstag')),
                ('athleticagen', models.CharField(max_length=1, db_column='Athleticagen')),
                ('bezahlt', models.CharField(max_length=1, db_column='Bezahlt')),
                ('xregion', models.IntegerField(db_column='xRegion')),
                ('lizenztyp', models.IntegerField(db_column='Lizenztyp')),
                ('manuell', models.IntegerField(db_column='Manuell')),
                ('adresse', models.CharField(max_length=50, db_column='Adresse', blank=True)),
                ('plz', models.IntegerField(null=True, db_column='Plz', blank=True)),
                ('ort', models.CharField(max_length=50, db_column='Ort', blank=True)),
                ('email', models.CharField(max_length=50, db_column='Email', blank=True)),
            ],
            options={
                'db_table': 'athlet',
                'verbose_name_plural': 'athleten',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='anmeldung',
            name='athlet',
            field=models.ForeignKey(related_name='anmeldungen', db_column='xAthlet', to='main.Athlet'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='BaseAccount',
        ),
        migrations.CreateModel(
            name='BaseAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_code', models.CharField(max_length=30)),
                ('account_name', models.CharField(max_length=255)),
                ('account_short', models.CharField(max_length=255)),
                ('account_type', models.CharField(max_length=100)),
                ('lg', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'base_account',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BaseAthlete',
        ),
        migrations.CreateModel(
            name='BaseAthlete',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('license', models.IntegerField()),
                ('license_paid', models.CharField(max_length=1)),
                ('license_cat', models.CharField(max_length=4)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=1)),
                ('nationality', models.CharField(max_length=3)),
                ('account_code', models.CharField(max_length=30)),
                ('second_account_code', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('account_info', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'base_athlete',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BaseLog',
        ),
        migrations.CreateModel(
            name='BaseLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('update_time', models.DateTimeField()),
                ('global_last_change', models.DateField()),
            ],
            options={
                'db_table': 'base_log',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BasePerformance',
        ),
        migrations.CreateModel(
            name='BasePerformance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('id_athlete', models.IntegerField()),
                ('discipline', models.IntegerField()),
                ('category', models.CharField(max_length=10)),
                ('best_effort', models.CharField(max_length=15)),
                ('best_effort_date', models.DateField()),
                ('best_effort_event', models.CharField(max_length=100)),
                ('season_effort', models.CharField(max_length=15)),
                ('season_effort_date', models.DateField()),
                ('season_effort_event', models.CharField(max_length=100)),
                ('notification_effort', models.CharField(max_length=15)),
                ('notification_effort_date', models.DateField()),
                ('notification_effort_event', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'base_performance',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BaseRelay',
        ),
        migrations.CreateModel(
            name='BaseRelay',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_athletica_gen', models.CharField(max_length=1)),
                ('relay_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=10)),
                ('discipline', models.CharField(max_length=10)),
                ('account_code', models.IntegerField()),
            ],
            options={
                'db_table': 'base_relay',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BaseSvm',
        ),
        migrations.CreateModel(
            name='BaseSvm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_athletica_gen', models.CharField(max_length=1)),
                ('svm_name', models.CharField(max_length=255)),
                ('svm_category', models.CharField(max_length=10)),
                ('account_code', models.IntegerField()),
            ],
            options={
                'db_table': 'base_svm',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='DisziplinDe',
        ),
        migrations.CreateModel(
            name='DisziplinDe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xDisziplin')),
                ('kurzname', models.CharField(unique=True, max_length=15, db_column='Kurzname')),
                ('name', models.CharField(max_length=40, db_column='Name')),
                ('anzeige', models.IntegerField(db_column='Anzeige')),
                ('seriegroesse', models.IntegerField(db_column='Seriegroesse')),
                ('staffellaeufer', models.IntegerField(null=True, db_column='Staffellaeufer', blank=True)),
                ('typ', models.IntegerField(db_column='Typ')),
                ('appellzeit', models.TimeField(db_column='Appellzeit')),
                ('stellzeit', models.TimeField(db_column='Stellzeit')),
                ('strecke', models.FloatField(db_column='Strecke')),
                ('code', models.IntegerField(db_column='Code')),
                ('xomega_typ', models.IntegerField(db_column='xOMEGA_Typ')),
                ('aktiv', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'disziplin_de',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='DisziplinFr',
        ),
        migrations.CreateModel(
            name='DisziplinFr',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xDisziplin')),
                ('kurzname', models.CharField(unique=True, max_length=15, db_column='Kurzname')),
                ('name', models.CharField(max_length=40, db_column='Name')),
                ('anzeige', models.IntegerField(db_column='Anzeige')),
                ('seriegroesse', models.IntegerField(db_column='Seriegroesse')),
                ('staffellaeufer', models.IntegerField(null=True, db_column='Staffellaeufer', blank=True)),
                ('typ', models.IntegerField(db_column='Typ')),
                ('appellzeit', models.TimeField(db_column='Appellzeit')),
                ('stellzeit', models.TimeField(db_column='Stellzeit')),
                ('strecke', models.FloatField(db_column='Strecke')),
                ('code', models.IntegerField(db_column='Code')),
                ('xomega_typ', models.IntegerField(db_column='xOMEGA_Typ')),
                ('aktiv', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'disziplin_fr',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='DisziplinIt',
        ),
        migrations.CreateModel(
            name='DisziplinIt',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xDisziplin')),
                ('kurzname', models.CharField(unique=True, max_length=15, db_column='Kurzname')),
                ('name', models.CharField(max_length=40, db_column='Name')),
                ('anzeige', models.IntegerField(db_column='Anzeige')),
                ('seriegroesse', models.IntegerField(db_column='Seriegroesse')),
                ('staffellaeufer', models.IntegerField(null=True, db_column='Staffellaeufer', blank=True)),
                ('typ', models.IntegerField(db_column='Typ')),
                ('appellzeit', models.TimeField(db_column='Appellzeit')),
                ('stellzeit', models.TimeField(db_column='Stellzeit')),
                ('strecke', models.FloatField(db_column='Strecke')),
                ('code', models.IntegerField(db_column='Code')),
                ('xomega_typ', models.IntegerField(db_column='xOMEGA_Typ')),
                ('aktiv', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'disziplin_it',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Faq',
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xFaq')),
                ('frage', models.CharField(max_length=255, db_column='Frage')),
                ('antwort', models.TextField(db_column='Antwort')),
                ('zeigen', models.CharField(max_length=1, db_column='Zeigen')),
                ('postop', models.IntegerField(db_column='PosTop')),
                ('posleft', models.IntegerField(db_column='PosLeft')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('seite', models.CharField(max_length=255, db_column='Seite')),
                ('sprache', models.CharField(max_length=2, db_column='Sprache')),
                ('farbetitel', models.CharField(max_length=6, db_column='FarbeTitel')),
                ('farbehg', models.CharField(max_length=6, db_column='FarbeHG')),
            ],
            options={
                'db_table': 'faq',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Hoehe',
        ),
        migrations.CreateModel(
            name='Hoehe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xHoehe')),
                ('hoehe', models.IntegerField(db_column='Hoehe')),
                ('xrunde', models.IntegerField(db_column='xRunde')),
                ('xserie', models.IntegerField(db_column='xSerie')),
            ],
            options={
                'db_table': 'hoehe',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Kategorie',
        ),
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xKategorie')),
                ('kurzname', models.CharField(unique=True, max_length=4, db_column='Kurzname')),
                ('name', models.CharField(max_length=30, db_column='Name')),
                ('anzeige', models.IntegerField(db_column='Anzeige')),
                ('alterslimite', models.IntegerField(db_column='Alterslimite')),
                ('code', models.CharField(max_length=4, db_column='Code')),
                ('geschlecht', models.CharField(max_length=1, db_column='Geschlecht')),
                ('aktiv', models.CharField(max_length=1)),
                ('ukc', models.CharField(max_length=1, db_column='UKC', blank=True)),
            ],
            options={
                'db_table': 'kategorie',
                'verbose_name_plural': 'kategorien',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='anmeldung',
            name='kategorie',
            field=models.ForeignKey(related_name='-', db_column='xKategorie', to='main.Kategorie'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='KategorieSvm',
        ),
        migrations.CreateModel(
            name='KategorieSvm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xKategorie_svm')),
                ('name', models.CharField(max_length=100, db_column='Name')),
                ('code', models.CharField(max_length=5, db_column='Code')),
            ],
            options={
                'db_table': 'kategorie_svm',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Land',
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('xcode', models.CharField(max_length=3, serialize=False, primary_key=True, db_column='xCode')),
                ('name', models.CharField(max_length=100, db_column='Name')),
                ('sortierwert', models.IntegerField(db_column='Sortierwert')),
            ],
            options={
                'db_table': 'land',
                'verbose_name_plural': 'l\xe4nder',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Layout',
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('xlayout', models.IntegerField(serialize=False, primary_key=True, db_column='xLayout')),
                ('typtl', models.IntegerField(db_column='TypTL')),
                ('texttl', models.CharField(max_length=255, db_column='TextTL')),
                ('bildtl', models.CharField(max_length=255, db_column='BildTL')),
                ('typtc', models.IntegerField(db_column='TypTC')),
                ('texttc', models.CharField(max_length=255, db_column='TextTC')),
                ('bildtc', models.CharField(max_length=255, db_column='BildTC')),
                ('typtr', models.IntegerField(db_column='TypTR')),
                ('texttr', models.CharField(max_length=255, db_column='TextTR')),
                ('bildtr', models.CharField(max_length=255, db_column='BildTR')),
                ('typbl', models.IntegerField(db_column='TypBL')),
                ('textbl', models.CharField(max_length=255, db_column='TextBL')),
                ('bildbl', models.CharField(max_length=255, db_column='BildBL')),
                ('typbc', models.IntegerField(db_column='TypBC')),
                ('textbc', models.CharField(max_length=255, db_column='TextBC')),
                ('bildbc', models.CharField(max_length=255, db_column='BildBC')),
                ('typbr', models.IntegerField(db_column='TypBR')),
                ('textbr', models.CharField(max_length=255, db_column='TextBR')),
                ('bildbr', models.CharField(max_length=255, db_column='BildBR')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
            ],
            options={
                'db_table': 'layout',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='OmegaTyp',
        ),
        migrations.CreateModel(
            name='OmegaTyp',
            fields=[
                ('xomega_typ', models.IntegerField(serialize=False, primary_key=True, db_column='xOMEGA_Typ')),
                ('omega_name', models.CharField(max_length=15, db_column='OMEGA_Name')),
                ('omega_kurzname', models.CharField(max_length=4, db_column='OMEGA_Kurzname')),
            ],
            options={
                'db_table': 'omega_typ',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xRegion')),
                ('name', models.CharField(max_length=50, db_column='Name')),
                ('anzeige', models.CharField(max_length=6, db_column='Anzeige')),
                ('sortierwert', models.IntegerField(db_column='Sortierwert')),
                ('ukc', models.CharField(max_length=1, db_column='UKC', blank=True)),
            ],
            options={
                'db_table': 'region',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Resultat',
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xResultat')),
                ('leistung', models.IntegerField(db_column='Leistung')),
                ('info', models.CharField(max_length=5, db_column='Info')),
                ('punkte', models.FloatField(db_column='Punkte')),
            ],
            options={
                'db_table': 'resultat',
                'verbose_name_plural': 'resultate',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Runde',
        ),
        migrations.CreateModel(
            name='Runde',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xRunde')),
                ('datum', models.DateField(db_column='Datum')),
                ('startzeit', models.TimeField(db_column='Startzeit')),
                ('appellzeit', models.TimeField(db_column='Appellzeit')),
                ('stellzeit', models.TimeField(db_column='Stellzeit')),
                ('status', models.IntegerField(db_column='Status')),
                ('speakerstatus', models.IntegerField(db_column='Speakerstatus')),
                ('statuszeitmessung', models.IntegerField(db_column='StatusZeitmessung')),
                ('statusupload', models.IntegerField(db_column='StatusUpload')),
                ('qualifikationsieger', models.IntegerField(db_column='QualifikationSieger')),
                ('qualifikationleistung', models.IntegerField(db_column='QualifikationLeistung')),
                ('bahnen', models.IntegerField(db_column='Bahnen')),
                ('versuche', models.IntegerField(db_column='Versuche')),
                ('gruppe', models.CharField(max_length=2, db_column='Gruppe')),
                ('xrundentyp', models.IntegerField(null=True, db_column='xRundentyp', blank=True)),
                ('nurbestesresultat', models.CharField(max_length=1, db_column='nurBestesResultat')),
                ('statuschanged', models.CharField(max_length=1, db_column='StatusChanged')),
                ('endkampf', models.CharField(max_length=1, db_column='Endkampf')),
                ('finalisten', models.IntegerField(null=True, db_column='Finalisten', blank=True)),
                ('finalnach', models.IntegerField(null=True, db_column='FinalNach', blank=True)),
                ('drehen', models.CharField(max_length=20, db_column='Drehen', blank=True)),
                ('statusuploadukc', models.IntegerField(null=True, db_column='StatusUploadUKC', blank=True)),
            ],
            options={
                'db_table': 'runde',
                'verbose_name_plural': 'runden',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Rundenlog',
        ),
        migrations.CreateModel(
            name='Rundenlog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xRundenlog')),
                ('zeit', models.DateTimeField(db_column='Zeit')),
                ('ereignis', models.CharField(max_length=255, db_column='Ereignis')),
                ('runde', models.ForeignKey(related_name='rundenlog', db_column='xRunde', to='main.Runde')),
            ],
            options={
                'db_table': 'rundenlog',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Rundenset',
        ),
        migrations.CreateModel(
            name='Rundenset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xrundenset', models.IntegerField(db_column='xRundenset')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
                ('xrunde', models.IntegerField(db_column='xRunde')),
                ('hauptrunde', models.IntegerField(db_column='Hauptrunde')),
            ],
            options={
                'db_table': 'rundenset',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='RundentypDe',
        ),
        migrations.CreateModel(
            name='RundentypDe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xRundentyp')),
                ('typ', models.CharField(unique=True, max_length=2, db_column='Typ')),
                ('name', models.CharField(unique=True, max_length=20, db_column='Name')),
                ('wertung', models.IntegerField(null=True, db_column='Wertung', blank=True)),
                ('code', models.CharField(max_length=2, db_column='Code')),
            ],
            options={
                'db_table': 'rundentyp_de',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='RundentypFr',
        ),
        migrations.CreateModel(
            name='RundentypFr',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xRundentyp')),
                ('typ', models.CharField(unique=True, max_length=2, db_column='Typ')),
                ('name', models.CharField(unique=True, max_length=20, db_column='Name')),
                ('wertung', models.IntegerField(null=True, db_column='Wertung', blank=True)),
                ('code', models.CharField(max_length=2, db_column='Code')),
            ],
            options={
                'db_table': 'rundentyp_fr',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='RundentypIt',
        ),
        migrations.CreateModel(
            name='RundentypIt',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xRundentyp')),
                ('typ', models.CharField(unique=True, max_length=2, db_column='Typ')),
                ('name', models.CharField(unique=True, max_length=20, db_column='Name')),
                ('wertung', models.IntegerField(null=True, db_column='Wertung', blank=True)),
                ('code', models.CharField(max_length=2, db_column='Code')),
            ],
            options={
                'db_table': 'rundentyp_it',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Serie',
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xSerie')),
                ('bezeichnung', models.CharField(max_length=2, db_column='Bezeichnung')),
                ('wind', models.CharField(max_length=5, db_column='Wind', blank=True)),
                ('film', models.IntegerField(null=True, db_column='Film', blank=True)),
                ('status', models.IntegerField(db_column='Status')),
                ('handgestoppt', models.IntegerField(db_column='Handgestoppt')),
                ('tvname', models.CharField(max_length=70, db_column='TVName', blank=True)),
                ('maxathlet', models.IntegerField(db_column='MaxAthlet')),
                ('runde', models.ForeignKey(related_name='serien', db_column='xRunde', to='main.Runde')),
                ('anlage', models.ForeignKey(db_column='xAnlage', blank=True, to='main.Anlage', null=True)),
            ],
            options={
                'db_table': 'serie',
                'verbose_name_plural': 'serien',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Serienstart',
        ),
        migrations.CreateModel(
            name='Serienstart',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xSerienstart')),
                ('position', models.IntegerField(db_column='Position')),
                ('bahn', models.IntegerField(db_column='Bahn')),
                ('rang', models.IntegerField(db_column='Rang')),
                ('qualifikation', models.IntegerField(db_column='Qualifikation')),
                ('rundezusammen', models.IntegerField(db_column='RundeZusammen')),
                ('bemerkung', models.CharField(max_length=5, db_column='Bemerkung')),
                ('position2', models.IntegerField(db_column='Position2')),
                ('position3', models.IntegerField(db_column='Position3')),
                ('aktivathlet', models.CharField(max_length=1, db_column='AktivAthlet')),
                ('starthoehe', models.IntegerField(null=True, db_column='Starthoehe', blank=True)),
                ('serie', models.ForeignKey(related_name='serienstarts', db_column='xSerie', to='main.Serie')),
            ],
            options={
                'db_table': 'serienstart',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='resultat',
            name='serienstart',
            field=models.ForeignKey(related_name='resultat', db_column='xSerienstart', to='main.Serienstart'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Staffel',
        ),
        migrations.CreateModel(
            name='Staffel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xStaffel')),
                ('name', models.CharField(max_length=40, db_column='Name')),
                ('xverein', models.IntegerField(db_column='xVerein')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
                ('xkategorie', models.IntegerField(db_column='xKategorie')),
                ('xteam', models.IntegerField(db_column='xTeam')),
                ('athleticagen', models.CharField(max_length=1, db_column='Athleticagen')),
                ('startnummer', models.IntegerField(db_column='Startnummer')),
            ],
            options={
                'db_table': 'staffel',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Staffelathlet',
        ),
        migrations.CreateModel(
            name='Staffelathlet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xstaffelstart', models.IntegerField(db_column='xStaffelstart')),
                ('xathletenstart', models.IntegerField(db_column='xAthletenstart')),
                ('xrunde', models.IntegerField(db_column='xRunde')),
                ('position', models.IntegerField(db_column='Position')),
            ],
            options={
                'db_table': 'staffelathlet',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Start',
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xStart')),
                ('anwesend', models.IntegerField(db_column='Anwesend')),
                ('bestleistung', models.IntegerField(db_column='Bestleistung')),
                ('bezahlt', models.CharField(max_length=1, db_column='Bezahlt')),
                ('erstserie', models.CharField(max_length=1, db_column='Erstserie')),
                ('baseeffort', models.CharField(max_length=1, db_column='BaseEffort')),
                ('vorjahrleistung', models.IntegerField(null=True, db_column='VorjahrLeistung', blank=True)),
                ('gruppe', models.CharField(max_length=2, db_column='Gruppe', blank=True)),
                ('staffel', models.ForeignKey(to='main.Staffel', db_column='xStaffel')),
                ('anmeldung', models.ForeignKey(related_name='starts', db_column='xAnmeldung', to='main.Anmeldung')),
            ],
            options={
                'db_table': 'start',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='serienstart',
            name='start',
            field=models.ForeignKey(related_name='serienstart', db_column='xStart', to='main.Start'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='SysBackuptabellen',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xTeam')),
                ('name', models.CharField(max_length=30, db_column='Name')),
                ('athleticagen', models.CharField(max_length=1, db_column='Athleticagen')),
                ('xkategorie', models.IntegerField(db_column='xKategorie')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
                ('xverein', models.IntegerField(db_column='xVerein')),
                ('xkategorie_svm', models.IntegerField(db_column='xKategorie_svm')),
            ],
            options={
                'db_table': 'team',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Teamsm',
        ),
        migrations.CreateModel(
            name='Teamsm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xTeamsm')),
                ('name', models.CharField(max_length=100, db_column='Name')),
                ('xkategorie', models.IntegerField(db_column='xKategorie')),
                ('xverein', models.IntegerField(db_column='xVerein')),
                ('xwettkampf', models.IntegerField(db_column='xWettkampf')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
                ('startnummer', models.IntegerField(db_column='Startnummer')),
                ('gruppe', models.CharField(max_length=2, db_column='Gruppe', blank=True)),
                ('quali', models.IntegerField(db_column='Quali')),
                ('leistung', models.IntegerField(db_column='Leistung')),
            ],
            options={
                'db_table': 'teamsm',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Teamsmathlet',
        ),
        migrations.CreateModel(
            name='Teamsmathlet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xteamsm', models.IntegerField(db_column='xTeamsm')),
                ('xanmeldung', models.IntegerField(db_column='xAnmeldung')),
            ],
            options={
                'db_table': 'teamsmathlet',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Verein',
        ),
        migrations.CreateModel(
            name='Verein',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xVerein')),
                ('name', models.CharField(unique=True, max_length=100, db_column='Name')),
                ('sortierwert', models.CharField(max_length=100, db_column='Sortierwert')),
                ('xcode', models.CharField(max_length=30, db_column='xCode')),
                ('geloescht', models.IntegerField(db_column='Geloescht')),
            ],
            options={
                'db_table': 'verein',
                'verbose_name_plural': 'vereine',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='athlet',
            name='verein',
            field=models.ForeignKey(related_name='athleten', db_column='xVerein', to='main.Verein'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Videowand',
        ),
        migrations.CreateModel(
            name='Videowand',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xVideowand')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
                ('x', models.IntegerField(db_column='X')),
                ('y', models.IntegerField(db_column='Y')),
                ('inhaltart', models.CharField(max_length=4, db_column='InhaltArt')),
                ('inhaltstatisch', models.TextField(db_column='InhaltStatisch')),
                ('inhaltdynamisch', models.TextField(db_column='InhaltDynamisch')),
                ('aktualisierung', models.IntegerField(db_column='Aktualisierung')),
                ('status', models.CharField(max_length=6, db_column='Status')),
                ('hintergrund', models.CharField(max_length=6, db_column='Hintergrund')),
                ('fordergrund', models.CharField(max_length=6, db_column='Fordergrund')),
                ('bildnr', models.IntegerField(db_column='Bildnr')),
            ],
            options={
                'db_table': 'videowand',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Wertungstabelle',
        ),
        migrations.CreateModel(
            name='Wertungstabelle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xWertungstabelle')),
                ('name', models.CharField(max_length=255, db_column='Name')),
            ],
            options={
                'db_table': 'wertungstabelle',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='WertungstabellePunkte',
        ),
        migrations.CreateModel(
            name='WertungstabellePunkte',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xWertungstabelle_Punkte')),
                ('xwertungstabelle', models.IntegerField(db_column='xWertungstabelle')),
                ('xdisziplin', models.IntegerField(db_column='xDisziplin')),
                ('geschlecht', models.CharField(max_length=1, db_column='Geschlecht')),
                ('leistung', models.CharField(max_length=50, db_column='Leistung')),
                ('punkte', models.FloatField(db_column='Punkte')),
            ],
            options={
                'db_table': 'wertungstabelle_punkte',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Wettkampf',
        ),
        migrations.CreateModel(
            name='Wettkampf',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xWettkampf')),
                ('typ', models.IntegerField(db_column='Typ')),
                ('haftgeld', models.FloatField(db_column='Haftgeld')),
                ('startgeld', models.FloatField(db_column='Startgeld')),
                ('punktetabelle', models.IntegerField(db_column='Punktetabelle')),
                ('punkteformel', models.CharField(max_length=20, db_column='Punkteformel')),
                ('windmessung', models.IntegerField(db_column='Windmessung')),
                ('info', models.CharField(max_length=50, db_column='Info', blank=True)),
                ('zeitmessung', models.IntegerField(db_column='Zeitmessung')),
                ('zeitmessungauto', models.IntegerField(db_column='ZeitmessungAuto')),
                ('mehrkampfcode', models.IntegerField(db_column='Mehrkampfcode')),
                ('mehrkampfende', models.IntegerField(db_column='Mehrkampfende')),
                ('mehrkampfreihenfolge', models.IntegerField(db_column='Mehrkampfreihenfolge')),
                ('xkategorie_svm', models.IntegerField(db_column='xKategorie_svm')),
                ('onlineid', models.IntegerField(db_column='OnlineId')),
                ('typaenderung', models.CharField(max_length=50, db_column='TypAenderung')),
                ('meeting', models.ForeignKey(related_name='wettkaempfe', db_column='xMeeting', to='main.Meeting')),
                ('kategorie', models.ForeignKey(to='main.Kategorie', db_column='xKategorie')),
                ('disziplin', models.ForeignKey(to='main.DisziplinDe', db_column='xDisziplin')),
            ],
            options={
                'db_table': 'wettkampf',
                'verbose_name_plural': 'wettk\xe4mpfe',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='runde',
            name='wettkampf',
            field=models.ForeignKey(related_name='runden', db_column='xWettkampf', to='main.Wettkampf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='start',
            name='wettkampf',
            field=models.ForeignKey(related_name='starts', db_column='xWettkampf', to='main.Wettkampf'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Zeitmessung',
        ),
        migrations.CreateModel(
            name='Zeitmessung',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='xZeitmessung')),
                ('omega_verbindung', models.CharField(max_length=5, db_column='OMEGA_Verbindung')),
                ('omega_pfad', models.CharField(max_length=255, db_column='OMEGA_Pfad')),
                ('omega_server', models.CharField(max_length=255, db_column='OMEGA_Server')),
                ('omega_benutzer', models.CharField(max_length=50, db_column='OMEGA_Benutzer')),
                ('omega_passwort', models.CharField(max_length=50, db_column='OMEGA_Passwort')),
                ('omega_ftppfad', models.CharField(max_length=255, db_column='OMEGA_Ftppfad')),
                ('omega_sponsor', models.CharField(max_length=255, db_column='OMEGA_Sponsor')),
                ('alge_typ', models.CharField(max_length=20, db_column='ALGE_Typ')),
                ('alge_ftppfad', models.CharField(max_length=255, db_column='ALGE_Ftppfad')),
                ('alge_passwort', models.CharField(max_length=50, db_column='ALGE_Passwort')),
                ('alge_benutzer', models.CharField(max_length=50, db_column='ALGE_Benutzer')),
                ('alge_server', models.CharField(max_length=255, db_column='ALGE_Server')),
                ('alge_pfad', models.CharField(max_length=255, db_column='ALGE_Pfad')),
                ('alge_verbindung', models.CharField(max_length=5, db_column='ALGE_Verbindung')),
                ('xmeeting', models.IntegerField(db_column='xMeeting')),
            ],
            options={
                'db_table': 'zeitmessung',
            },
            bases=(models.Model,),
        ),
    ]