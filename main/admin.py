from django.contrib import admin

from main.models import Anlage
admin.site.register(Anlage)
class AnlageInline(admin.TabularInline):
    model = Anlage
    fieldsets = [(None, {'fields': ['bezeichnung', 'homologiert']}),]
    extra = 0
from main.models import Anmeldung
admin.site.register(Anmeldung)
from main.models import Athlet
admin.site.register(Athlet)
from main.models import Kategorie
admin.site.register(Kategorie)
from main.models import Land
admin.site.register(Land)
from main.models import Meeting
class MeetingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Meeting, MeetingAdmin)
from main.models import Resultat
admin.site.register(Resultat)
from main.models import Runde
admin.site.register(Runde)
from main.models import Rundenlog
admin.site.register(Rundenlog)
from main.models import Serie
admin.site.register(Serie)
from main.models import Serienstart
admin.site.register(Serienstart)
from main.models import Stadion
class StadionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {
        'fields': ['name', 'bahnen', 'bahnengerade', 'ueber1000m', 'halle']}),]
    inlines = [AnlageInline]
admin.site.register(Stadion, StadionAdmin)
from main.models import Start
admin.site.register(Start)
from main.models import Verein
admin.site.register(Verein)
from main.models import Wettkampf
admin.site.register(Wettkampf)
