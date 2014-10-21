from django.contrib import admin

from main.models import Anlage
admin.site.register(Anlage)
from main.models import Anmeldung
admin.site.register(Anmeldung)
from main.models import Meeting
admin.site.register(Meeting)

