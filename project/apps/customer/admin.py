from . import models
from django.contrib import admin

# Register your models here.
admin.site.site_title = "customer"
# admin.site.register(Customer, CustomerAdmin)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname", "phone",
                    "email", "dni", "numero_cliente")
    # list_filter = ()
    search_fields = ("name", "lastname", "dni")
