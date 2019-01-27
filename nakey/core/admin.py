from django.contrib import admin
from .models import *


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ItemImageAdmin(admin.StackedInline):
    model = ItemImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    search_fields = ('name',)
    inlines = (ItemImageAdmin,)


class RequestItemAdmin(admin.StackedInline):
    model = RequestItem
    readonly_fields = ('item', 'count')


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'address', 'email')
    search_fields = ('full_name',)
    inlines = (RequestItemAdmin,)
