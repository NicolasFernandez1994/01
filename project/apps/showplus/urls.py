from django.urls import path

from .views import home

app_name = "showplus"


urlpatterns = [
    path("", home, name="home"),
]