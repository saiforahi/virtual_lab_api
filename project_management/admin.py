from django.contrib import admin
from project_management.models import Project, ProjectTool


# Register your models here.


class ProjectToolInlineAdmin(admin.StackedInline):
    model = ProjectTool
    extra = 0
    min_num = 1


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('schedule', 'name', 'owner','diagram','extra_instruction')}),
    )
    list_display = ['name','owner','diagram']
    inlines = [ProjectToolInlineAdmin]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTool)
