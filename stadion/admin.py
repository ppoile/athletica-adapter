from django.contrib import admin

from main.models import Anlage
from stadion.models import Stadion

class AnlageInline(admin.TabularInline):
    model = Anlage
    fieldsets = [(None, {'fields': ['bezeichnung', 'homologiert']}),]
    extra = 0

class StadionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {
        'fields': ['name', 'bahnen', 'bahnengerade', 'ueber1000m', 'halle']}),]
    inlines = [AnlageInline]

admin.site.register(Stadion, StadionAdmin)
