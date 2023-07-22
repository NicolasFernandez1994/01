from django.urls import path

from .views import home

app_name = "Nosotros"

urlpatterns = [
    path("", home, name="home"),
]
