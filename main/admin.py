from django.contrib import admin

# Register your models here.
from main.models import Stadion, Anlage

admin.site.register(Anlage)
admin.site.register(Stadion)
