from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from main.models import UserD


class UserDInline(admin.StackedInline):
    model = UserD
    can_delete = False
    verbose_name_plural = 'UserDefault'


class UserAdmin(BaseUserAdmin):
    inlines = (UserDInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)