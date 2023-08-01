from django.contrib import admin

from . import models

admin.site.site_title = "Productos"

admin.site.register(models.ProductoCategoriaa)


@admin.register(models.ProductoCategoriaa)
class ProductoCategoriaaAdmin(admin.ModelAdmin):
    list_display = ("articulo", "marca", "codigo", "descripcion")
    list_filter = ("articulo",)
    search_fields = ("articulo", "marca")
    ordering = ("articulo",)
