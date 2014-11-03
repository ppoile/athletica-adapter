from django.contrib import admin

from stadion.models import Anlage
from stadion.models import Stadion

admin.site.register(Anlage)

class AnlageInline(admin.TabularInline):
    model = Anlage
    fieldsets = [(None, {'fields': ['bezeichnung', 'homologiert']}),]
    extra = 0

class StadionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {
        'fields': ['name', 'bahnen', 'bahnengerade', 'ueber1000m', 'halle']}),]
    inlines = [AnlageInline]

admin.site.register(Stadion, StadionAdmin)
