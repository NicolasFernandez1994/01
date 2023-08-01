from unicodedata import category
from django.shortcuts import render

from . import models


# Pagina Principal
def index(request):
    contexto = {"app": "Aplicación Producto"}
    return render(request, "producto/index.html")

# Crear Producto

# Lista Producto


def list_product(request):
    categorias = models.ProductoCategoriaa.objects.all()
    context = {"objects_list": categorias}
    return render(request, "producto/02lista_productos.html", context)
