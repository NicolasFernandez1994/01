from django.urls import path

from . import views

# from .views import home

app_name = "producto"

urlpatterns = [
    path("", views.index, name="home"),
    path("02lista_productos/list/", views.list_product, name="02lista_productos"),
]
