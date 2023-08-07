from django.urls import path
from django.views.generic import TemplateView

from . import views

# from .views import home

app_name = "customerx"

urlpatterns = [
    path("", views.home, name="home"),
    path("02lista_customerx/list/", views.list_customerx, name="02lista_customerx"),
    path("01crear_customerx/create/",
         views.create_customerx, name="01crear_customerx"),
    path("03detail_customerx/<int:pk>/",
         views.detail_customerx, name="03detail_customerx"),
    path("04actualizar_customerx/<int:pk>/",
         views.update_customerx, name="01crear_customerx"),
    path("05delete_customerx/<int:pk>/",
         views.delete_customerx, name="05delete_customerx"),
]
