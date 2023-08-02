from django.urls import path

from .views import home

app_name = "productosventa"


urlpatterns = [
    path("", home, name="home"),
]