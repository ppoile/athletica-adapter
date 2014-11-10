athletica-adapter
=================

Adapter to Athletica

Overview
--------

Athletica-adapter is a Django project.

It is named 'athletica'.
It consists of the following apps:
# Meeting
## Definition
## Anmeldungen
# Wettkampf
## Appell
## Serien
## Resultate
## Ranglisten
# Administration
## Kategorien
## Disziplinen
## Vereine
## Aathleten
## Stadien

Doc
---

Model dependencies can be generated as follows:
> python manage.py graph_models stadion meeting main | dot -T pdf > athletica-models.pdf

Rangliste
---------
5.  Saurenmann Beat, 89, LV Winterthur, SUI, <punkte>, <bemerkung>
    100 (12.66 / 0,0 m, 527), WEIT (5.20 / -1.3, 421), KUGEL7.26 (9.92, 481),
    HOCH (1.55, 426), 400 (57.31, 509), 110H106.7 (19.71 / 0,0 m, 372),
    DISKUS2.00 (30.00, 464), STAB (3.00, 357), SPEER800 (41.03, 457),
    1500 (5:09.08, 509)

    Emry Guy 77 LV Winterthur, <land>, <punkte>, <bemerkung>
    100 (12.30 / 0,0 m, 593), WEIT (5.34 / -1.1, 449), KUGEL7.26 (11.78, 593),
    HOCH (1.75, 585), 400 (56.82, 528), 110H106.7 (16.77 / 0,0 m, 648),
    DISKUS2.00 (35.38, 571), STAB (3.20, 406), SPEER800 (-1, n.a.),
    1500 (-1, n.a.)
