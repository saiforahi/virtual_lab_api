from django.contrib import admin

from schedules.forms import ScheduleCreateForm, ScheduleChangeForm
from schedules.models import Schedule
from django.db import models
from django.forms import widgets
# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleChangeForm
    add_form = ScheduleCreateForm
    formfield_overrides = {
        models.TimeField: {'widget': widgets.TimeInput(format='%H:%M %p')}
    }
    fieldsets = (
        (None, {'fields': ('test_bed', 'date', 'start_time', 'end_time', 'is_available')}),
    )


admin.site.register(Schedule,ScheduleAdmin)