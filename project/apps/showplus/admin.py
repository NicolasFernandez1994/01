from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Showplus

# admin.site.register(Showplus)

from django.contrib import admin

from . import models

admin.site.site_title = "Showplus"


@admin.register(models.Showplus)
class ShowplusAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono", "descripcion", "precio")
    list_filter = ("nombre")
    search_fields = ("nombre")
