from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from main.models import UserD, Address, Category, Color, Size, Product, Image, Order, Menu, Setting , Order_list , Order_item , modal_connect


class UserDInline(admin.StackedInline):
    model = UserD
    can_delete = False
    verbose_name_plural = 'UserDefault'


class UserAdmin(BaseUserAdmin):
    inlines = (UserDInline,)


class SizeInline(admin.TabularInline):
    extra = 0
    model = Size


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ColorInline(SuperInlineModelAdmin, admin.StackedInline):
    extra = 0
    model = Color
    inlines = [ImageInline]


@admin.register(Product)
class ProductAdmin(SuperModelAdmin):
    inlines = [SizeInline, ColorInline]


class Order_item(admin.TabularInline):
    model = Order_item
    extra = 0

@admin.register(Order_list)
class OrederListAdmin(admin.ModelAdmin):
    inlines = (Order_item,)
    # exclude = ['post_code','City','stree','house','appartaments','comment']
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Address)
admin.site.register(Category)
# admin.site.register(Color)
# admin.site.register(Size)
# admin.site.register(Product)
# admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Setting)
admin.site.register(modal_connect)