# -*- coding: utf-8 -*-



def test_meeting():
    """test various meeting relations

>>> from meeting.models import Meeting

Die 10KAMPF_M-Wettkaempfe (Disziplinen):

>>> Meeting.objects.get(id=2).wettkaempfe.filter(info="10KAMPF_M", kategorie__name="MAN")
[<Wettkampf: 100 (10KAMPF_M)>, <Wettkampf: WEIT (10KAMPF_M)>, <Wettkampf: KUGEL (10KAMPF_M)>, <Wettkampf: HOCH (10KAMPF_M)>, <Wettkampf: 400 (10KAMPF_M)>, <Wettkampf: 110H (10KAMPF_M)>, <Wettkampf: DISKUS (10KAMPF_M)>, <Wettkampf: STAB (10KAMPF_M)>, <Wettkampf: SPEER (10KAMPF_M)>, <Wettkampf: 1500 (10KAMPF_M)>]

Die erste 10KAMPF_M-Disziplin:

>>> wettkampf = Meeting.objects.get(id=2).wettkaempfe.filter(info="10KAMPF_M", kategorie__name="MAN").first()
>>> wettkampf
<Wettkampf: 100 (10KAMPF_M)>

Die 10KAMPF_M-Resultate:

>>> from main.models import Start
>>> starts = Start.objects.filter(wettkampf__meeting_id=2).filter(wettkampf__info="10KAMPF_M", wettkampf__kategorie__name="MAN")
>>> len(starts)
60

>>> [(start.anmeldung.athlet,
...     (start.wettkampf.punkteformel,
...     (start.serienstart.first().resultat.first().leistung,
...     start.serienstart.first().resultat.first().punkte,
...     start.serienstart.first().rang)))
...     for start in starts]
[(<Athlet: Guy Emry>, (u'100', (12299L, 593.0, 2L))), (<Athlet: Benedikt Bühler>, (u'100', (12609L, 536.0, 5L))), (<Athlet: Roger Rüegg>, (u'100', (11835L, 683.0, 1L))), (<Athlet: Beat Saurenmann>, (u'100', (12659L, 527.0, 6L))), (<Athlet: Andrin Stucki>, (u'100', (12346L, 584.0, 3L))), (<Athlet: Markus Glaus>, (u'100', (12391L, 574.0, 4L))), (<Athlet: Guy Emry>, (u'WEIT', (534L, 449.0, 4L))), (<Athlet: Benedikt Bühler>, (u'WEIT', (546L, 473.0, 3L))), (<Athlet: Roger Rüegg>, (u'WEIT', (594L, 574.0, 1L))), (<Athlet: Beat Saurenmann>, (u'WEIT', (520L, 421.0, 6L))), (<Athlet: Andrin Stucki>, (u'WEIT', (564L, 510.0, 2L))), (<Athlet: Markus Glaus>, (u'WEIT', (515L, 411.0, 5L))), (<Athlet: Guy Emry>, (u'KUGEL', (1178L, 593.0, 2L))), (<Athlet: Benedikt Bühler>, (u'KUGEL', (1252L, 638.0, 1L))), (<Athlet: Roger Rüegg>, (u'KUGEL', (1087L, 538.0, 3L))), (<Athlet: Beat Saurenmann>, (u'KUGEL', (-98L, 0.0, 5L))), (<Athlet: Andrin Stucki>, (u'KUGEL', (926L, 441.0, 6L))), (<Athlet: Markus Glaus>, (u'KUGEL', (1053L, 518.0, 4L))), (<Athlet: Guy Emry>, (u'HOCH', (160L, 464.0, 1L))), (<Athlet: Benedikt Bühler>, (u'HOCH', (155L, 426.0, 5L))), (<Athlet: Roger Rüegg>, (u'HOCH', (160L, 464.0, 3L))), (<Athlet: Beat Saurenmann>, (u'HOCH', (150L, 389.0, 6L))), (<Athlet: Andrin Stucki>, (u'HOCH', (165L, 504.0, 2L))), (<Athlet: Markus Glaus>, (u'HOCH', (155L, 426.0, 3L))), (<Athlet: Guy Emry>, (u'400', (56820L, 528.0, 3L))), (<Athlet: Benedikt Bühler>, (u'400', (59400L, 434.0, 6L))), (<Athlet: Roger Rüegg>, (u'400', (53870L, 645.0, 1L))), (<Athlet: Beat Saurenmann>, (u'400', (57310L, 509.0, 5L))), (<Athlet: Andrin Stucki>, (u'400', (56240L, 550.0, 2L))), (<Athlet: Markus Glaus>, (u'400', (57180L, 514.0, 4L))), (<Athlet: Guy Emry>, (u'110H', (16768L, 648.0, 2L))), (<Athlet: Benedikt Bühler>, (u'110H', (19611L, 380.0, 5L))), (<Athlet: Roger Rüegg>, (u'110H', (16627L, 663.0, 1L))), (<Athlet: Beat Saurenmann>, (u'110H', (19705L, 372.0, 6L))), (<Athlet: Andrin Stucki>, (u'110H', (17976L, 526.0, 4L))), (<Athlet: Markus Glaus>, (u'110H', (16919L, 633.0, 3L))), (<Athlet: Guy Emry>, (u'DISKUS', (3538L, 571.0, 1L))), (<Athlet: Benedikt Bühler>, (u'DISKUS', (3348L, 533.0, 2L))), (<Athlet: Roger Rüegg>, (u'DISKUS', (3232L, 510.0, 4L))), (<Athlet: Beat Saurenmann>, (u'DISKUS', (3000L, 464.0, 6L))), (<Athlet: Andrin Stucki>, (u'DISKUS', (3237L, 511.0, 3L))), (<Athlet: Markus Glaus>, (u'DISKUS', (3228L, 509.0, 5L))), (<Athlet: Guy Emry>, (u'STAB', (280L, 309.0, 4L))), (<Athlet: Benedikt Bühler>, (u'STAB', (280L, 309.0, 3L))), (<Athlet: Roger Rüegg>, (u'STAB', (350L, 482.0, 2L))), (<Athlet: Beat Saurenmann>, (u'STAB', (280L, 309.0, 5L))), (<Athlet: Andrin Stucki>, (u'STAB', (360L, 509.0, 1L))), (<Athlet: Markus Glaus>, (u'STAB', (240L, 220.0, 5L))), (<Athlet: Guy Emry>, (u'SPEER', (-1L, 0.0, 0L))), (<Athlet: Benedikt Bühler>, (u'SPEER', (4411L, 502.0, 3L))), (<Athlet: Roger Rüegg>, (u'SPEER', (4871L, 570.0, 1L))), (<Athlet: Beat Saurenmann>, (u'SPEER', (4103L, 457.0, 4L))), (<Athlet: Andrin Stucki>, (u'SPEER', (4571L, 525.0, 2L))), (<Athlet: Markus Glaus>, (u'SPEER', (3670L, 395.0, 5L))), (<Athlet: Guy Emry>, (u'1500', (-1L, 0.0, 0L))), (<Athlet: Benedikt Bühler>, (u'1500', (339217L, 355.0, 9L))), (<Athlet: Roger Rüegg>, (u'1500', (292896L, 601.0, 3L))), (<Athlet: Beat Saurenmann>, (u'1500', (309078L, 509.0, 6L))), (<Athlet: Andrin Stucki>, (u'1500', (332917L, 385.0, 8L))), (<Athlet: Markus Glaus>, (u'1500', (317825L, 461.0, 7L)))]
"""
