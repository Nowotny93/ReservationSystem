from django.contrib import admin

from reservation_system.menu.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('name', )


admin.site.register(Menu, MenuAdmin)
