from django.urls import path

from .views import home

app_name = "work"


urlpatterns = [
    path("", home, name="home"),
]
