from django.contrib import admin

from reservation_system.inventory.models import Table


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('name', )


admin.site.register(Table, TableAdmin)
