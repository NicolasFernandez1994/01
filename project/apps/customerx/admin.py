from . import models
from django.contrib import admin

# Register your models here.
admin.site.site_title = "customerx"
# admin.site.register(Customer, CustomerAdmin)


@admin.register(models.Customerx)
class CustomerxAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname",
                    "email", "dni", "numero_cliente")
    # list_filter = ()
    #search_fields = ("name", "lastname", "dni")
    #ordering = ("name",)
