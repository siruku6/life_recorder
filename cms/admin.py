from django.contrib import admin
from cms.models import Record, ActivityType, Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'activity_type', 'name')
    list_display_links = ('id', 'start', 'end', 'activity_type', 'name')


admin.site.register(Record)
admin.site.register(ActivityType)
admin.site.register(Activity, ActivityAdmin)
