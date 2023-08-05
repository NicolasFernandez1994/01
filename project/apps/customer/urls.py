from django.urls import path
from django.views.generic import TemplateView

from .views import busqueda, crear_customer, crear_customers, home

app_name = "customer"

urlpatterns = [
    path("", home, name="home"),
    path('crear_customers/', crear_customers, name="crear_customers"),
    path('crear/', crear_customer, name="crear"),
    path('busqueda/', busqueda, name="busqueda")
]
