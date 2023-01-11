from django.contrib import admin

from tools.models import ToolType, Tool, WidgetType
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


class ToolTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    list_display = (
        'name', 'created_at', 'updated_at'
    )
    list_display_links = ('name',)
    list_filter = ['name', ]
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class WidgetTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields':
                    ('name','specs',)
                }
         ),
    )

    list_display = (
        'name', 'created_at', 'updated_at'
    )
    list_display_links = ('name',)
    list_filter = ['name', ]
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }


class ToolAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('type','name', 'widget_type','user_values','mqtt_data')}),
    )

    list_display = (
        'name', 'type','widget_type', 'created_at', 'updated_at'
    )
    list_display_links = ('name',)
    list_filter = ['name', 'type','widget_type']
    search_fields = ('name', 'type')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }


# Register your models here.
admin.site.register(ToolType, ToolTypeAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(WidgetType,WidgetTypeAdmin)
