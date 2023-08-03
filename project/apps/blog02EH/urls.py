from django.urls import path

from .views import home

app_name = "blog02EH"


urlpatterns = [
    path("", home, name="home"),
]