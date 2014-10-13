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
                'db_table': 'anlage',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Anmeldung',
            fields=[
            ],
            options={
                'db_table': 'anmeldung',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Athlet',
            fields=[
            ],
            options={
                'db_table': 'athlet',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseAccount',
            fields=[
            ],
            options={
                'db_table': 'base_account',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseAthlete',
            fields=[
            ],
            options={
                'db_table': 'base_athlete',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseLog',
            fields=[
            ],
            options={
                'db_table': 'base_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BasePerformance',
            fields=[
            ],
            options={
                'db_table': 'base_performance',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseRelay',
            fields=[
            ],
            options={
                'db_table': 'base_relay',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseSvm',
            fields=[
            ],
            options={
                'db_table': 'base_svm',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisziplinDe',
            fields=[
            ],
            options={
                'db_table': 'disziplin_de',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisziplinFr',
            fields=[
            ],
            options={
                'db_table': 'disziplin_fr',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisziplinIt',
            fields=[
            ],
            options={
                'db_table': 'disziplin_it',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
            ],
            options={
                'db_table': 'faq',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hoehe',
            fields=[
            ],
            options={
                'db_table': 'hoehe',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kategorie',
            fields=[
            ],
            options={
                'db_table': 'kategorie',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KategorieSvm',
            fields=[
            ],
            options={
                'db_table': 'kategorie_svm',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
            ],
            options={
                'db_table': 'land',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
            ],
            options={
                'db_table': 'layout',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
            ],
            options={
                'db_table': 'meeting',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OmegaTyp',
            fields=[
            ],
            options={
                'db_table': 'omega_typ',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
            ],
            options={
                'db_table': 'resultat',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runde',
            fields=[
            ],
            options={
                'db_table': 'runde',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rundenlog',
            fields=[
            ],
            options={
                'db_table': 'rundenlog',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rundenset',
            fields=[
            ],
            options={
                'db_table': 'rundenset',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RundentypDe',
            fields=[
            ],
            options={
                'db_table': 'rundentyp_de',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RundentypFr',
            fields=[
            ],
            options={
                'db_table': 'rundentyp_fr',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RundentypIt',
            fields=[
            ],
            options={
                'db_table': 'rundentyp_it',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
            ],
            options={
                'db_table': 'serie',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serienstart',
            fields=[
            ],
            options={
                'db_table': 'serienstart',
                'managed': False,
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staffel',
            fields=[
            ],
            options={
                'db_table': 'staffel',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staffelathlet',
            fields=[
            ],
            options={
                'db_table': 'staffelathlet',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
            ],
            options={
                'db_table': 'start',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SysBackuptabellen',
            fields=[
            ],
            options={
                'db_table': 'sys_backuptabellen',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teamsm',
            fields=[
            ],
            options={
                'db_table': 'teamsm',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teamsmathlet',
            fields=[
            ],
            options={
                'db_table': 'teamsmathlet',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verein',
            fields=[
            ],
            options={
                'db_table': 'verein',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Videowand',
            fields=[
            ],
            options={
                'db_table': 'videowand',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wertungstabelle',
            fields=[
            ],
            options={
                'db_table': 'wertungstabelle',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WertungstabellePunkte',
            fields=[
            ],
            options={
                'db_table': 'wertungstabelle_punkte',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wettkampf',
            fields=[
            ],
            options={
                'db_table': 'wettkampf',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zeitmessung',
            fields=[
            ],
            options={
                'db_table': 'zeitmessung',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
