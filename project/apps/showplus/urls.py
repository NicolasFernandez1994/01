from django.urls import path
from . import views
# from .views import home

app_name = "showplus"


urlpatterns = [
    path("", views.home, name="home"),
    path("", views.agregar_showplus, name="home"),
    path("02lista_showplus", views.list_showplus, name="02lista_showplus"),
    path("01crear_showplus", views.create_showplus, name="01crear_showplus"),
    path("03detail_showplus/<int:pk>/", views.detail_showplus, name="03detail_showplus"),
    path("04actualizar_showplus/<int:pk>/", views.update_showplus, name="01crear_showplus"),
    path("05delete_showplus/<int:pk>/", views.delete_showplus, name="05delete_showplus"),
]
