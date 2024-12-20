from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("item", "status", "type", "meal_type", "drink_type")

    list_filter = ("status",)

    search_fields = ("item", "description")


admin.site.register(Item, MenuItemAdmin)
