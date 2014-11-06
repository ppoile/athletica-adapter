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
