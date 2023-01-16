from django.contrib import admin
from project_management.models import Project, ProjectTool


# Register your models here.


class ProjectToolInlineAdmin(admin.StackedInline):
    model = ProjectTool
    extra = 0
    min_num = 1


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('schedule','name', 'owner', 'test_bed' ,'diagram', 'extra_instruction', 'status')}),
    )
    list_display = ['name', 'owner', 'schedule']
    list_filter = ['owner', 'schedule']
    inlines = [ProjectToolInlineAdmin]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class ProjectToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'schedule']
    list_filter = ['owner', 'schedule']
    inlines = [ProjectToolInlineAdmin]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTool)
