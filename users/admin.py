from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import UserChangeForm, UserCreationForm
from users.models import User


# Register your models here.


class UsersAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ', '.join(groups)

    group.short_description = 'Groups'

    fieldsets = (
        (None, {'fields': ('password', 'email')}),
        ('Profile info', {'fields': ('first_name', 'last_name', 'usr_profile_pic','age','gender' )}),
        ('Permissions',{'fields': ('groups', 'is_verified', 'is_active', 'is_staff', 'is_superuser',)}),
        ('Social Profiles', {'fields': ('fb_profile_link', 'twitter_profile_link', 'linkedin_profile_link')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email','phone','age','gender','groups', 'password1', 'password2')}
         ),
    )



    list_display = (
        'first_name','email','is_active','gender','group'
    )
    list_display_links = ('first_name','email')
    list_filter = ['groups', ]
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')


admin.site.register(User, UsersAdmin)