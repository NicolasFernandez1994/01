from django.contrib import admin

from . import models

admin.site.site_title = "Work"

@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "trabajo", "telefono")
    list_filter = ("nombre")
    search_fields = ("nombre")