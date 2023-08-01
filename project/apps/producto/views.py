from unicodedata import category
from django.shortcuts import redirect, render

from . import models
from . import forms

# Pagina Principal


def index(request):
    contexto = {"app": "Aplicación Producto"}
    return render(request, "producto/index.html")


# Lista Producto

def list_product(request):
    categorias = models.ProductoCategoriaa.objects.all()
    context = {"objects_list": categorias}
    return render(request, "producto/02lista_producto.html", context)

# Crear Producto


def create_product(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaaForm()
    return render(request, "producto/01crear_producto.html", {"form": form})
