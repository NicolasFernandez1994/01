from django.urls import path
from django.views.generic import TemplateView

from . import views

# from .views import home

app_name = "producto"

urlpatterns = [
    # path("", views.index, name="home"),
    path("", TemplateView.as_view(template_name="customer/index.html"), name="home"),
    path("02lista_customer/list/", views.list_customer, name="02lista_customer"),
    # path("02lista_productos/list/", views.02lista_producto, name="02lista_producto"),
    path("01crear_customer/create/",
         views.create_customer, name="01crear_customer"),
    path("03detail_customer/<int:pk>/",
         views.detail_customer, name="03detail_customer"),
    path("04actualizar_customer/<int:pk>/",
         views.update_customer, name="01crear_customer"),
    path("05delete_customer/<int:pk>/",
         views.delete_customer, name="05delete_customer"),
]
