from django.contrib import admin

from .models import *
# Register your models here.

class SurgeonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'birdhday', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', )

class WorkscheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'beforedinner', 'dinner', 'afterdinner', 'end', 'surg_id')
    list_display_links = ('id',)
    # list_editable = ('surg_id',)
    search_fields = ()

class ReceptiondaysAdmin(admin.ModelAdmin):
    list_display = ('id', 'monday', 'tuesday', 'wensday', 'thursday', 'friday', 'surg_id')
    list_display_links = ('id',)
    search_fields = ()

class ScheddeparturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'monday', 'tuesday', 'wensday', 'thursday', 'friday', 'surg_id')
    list_display_links = ('id',)
    search_fields = ()

class DutyAdmin(admin.ModelAdmin):
    list_display = ('id', 'month', 'day', 'dutytype', 'dutytime', 'dayornight', 'surg_id')
    list_display_links = ('id',)
    search_fields = ()

admin.site.register(Surgeon, SurgeonAdmin)
admin.site.register(Workschedule, WorkscheduleAdmin)
admin.site.register(Receptiondays, ReceptiondaysAdmin)
admin.site.register(Scheddepartures, ScheddeparturesAdmin)
admin.site.register(Duty, DutyAdmin)