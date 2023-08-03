from django.urls import path

from .views import home

app_name = "blog03PC"


urlpatterns = [
    path("", home, name="home"),
]
