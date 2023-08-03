from django.urls import path

from .views import home

app_name = "blog01JM"


urlpatterns = [
    path("", home, name="home"),
]
