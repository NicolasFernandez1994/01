from django.urls import path
from django.views.generic import TemplateView

from . import views

# from .views import home

app_name = "producto"

urlpatterns = [
    # path("", views.index, name="home"),
    path("", TemplateView.as_view(template_name="producto/index.html"), name="home"),
    path("02lista_productos/list/", views.list_product, name="02lista_producto"),
    # path("02lista_productos/list/", views.02lista_producto, name="02lista_producto"),
    path("01crear_producto/create/", views.create_product, name="01crear_producto"),
    path("03detail_producto/<int:pk>/",
         views.detail_product, name="03detail_producto"),
    path("04actualizar_producto/<int:pk>/",
         views.update_product, name="01crear_producto"),
    path("05delete_producto/<int:pk>/",
         views.delete_product, name="05delete_producto"),
]
