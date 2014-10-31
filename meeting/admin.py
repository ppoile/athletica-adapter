from django.contrib import admin

from meeting.models import Meeting

class MeetingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Meeting, MeetingAdmin)
