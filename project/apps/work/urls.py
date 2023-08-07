from django.urls import path
from . import views
from .views import home

app_name = "work"


urlpatterns = [
    path("", home, name="home"),
    path("", views.agregar_work, name="home"),
    path("02lista_work", views.list_work, name="02lista_work"),
    path("01crear_work", views.create_work, name="01crear_work"),
    path("03detail_work/<int:pk>/", views.detail_work, name="03detail_work"),
    path("04actualizar_work/<int:pk>/", views.update_work, name="01crear_work"),
    path("05delete_work/<int:pk>/", views.delete_work, name="05delete_work"),
]
