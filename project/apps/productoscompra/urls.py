from django.urls import path

from .views import home

app_name = "productoscompra"


urlpatterns = [
    path("", home, name="home"),
]