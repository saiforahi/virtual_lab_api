from django.contrib import admin

from tools.models import ToolType, Tool


class ToolTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    list_display = (
        'name','created_at','updated_at'
    )
    list_display_links = ('name',)
    list_filter = ['name', ]
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class ToolAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name','type',)}),
    )

    list_display = (
        'name','type','created_at','updated_at'
    )
    list_display_links = ('name',)
    list_filter = ['name','type']
    search_fields = ('name','type')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


# Register your models here.
admin.site.register(ToolType,ToolTypeAdmin)
admin.site.register(Tool,ToolAdmin)