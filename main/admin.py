from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from main.models import UserD, Address, Category, Color, Size, Product, Image, Order, Menu, Setting


class UserDInline(admin.StackedInline):
    model = UserD
    can_delete = False
    verbose_name_plural = 'UserDefault'


class UserAdmin(BaseUserAdmin):
    inlines = (UserDInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Setting)
