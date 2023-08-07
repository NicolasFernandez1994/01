from django.urls import path
from . import views
# from .views import home

app_name = "showplus"


urlpatterns = [
    path("", views.home, name="home"),
    path("", views.agregar_showplus, name="home"),
]
