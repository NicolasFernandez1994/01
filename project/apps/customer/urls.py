from django.urls import path

from .views import home

app_name = "customer"


urlpatterns = [
    path("", home, name="home"),
]
