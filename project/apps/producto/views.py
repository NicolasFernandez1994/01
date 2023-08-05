from unicodedata import category
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from . import models
from . import forms

# Pagina Principal


# def index(request):
# contexto = {"app": "Aplicación Producto"}
# return render(request, "producto/index.html")


# Lista Producto
def list_product(request):
    categorias = models.ProductoCategoriaa.objects.all()
    context = {"objects_list": categorias}
    return render(request, "producto/02lista_producto.html", context)

# class ProductoCategoriaaList (ListView):
    # model = models.ProductoCategoriaa

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

# Detalles Producto


def detail_product(request, pk):
    query = models.ProductoCategoriaa.objects.get(id=pk)
    return render(request, "producto/03detail_producto.html", {"object": query})

# Actualizar Producto


def update_product(request, pk):
    query = models.ProductoCategoriaa.objects.get(id=pk)
    if request.method == "POST":
        form = forms.ProductoCategoriaaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaaForm(instance=query)
    return render(request, "producto/01crear_producto.html", {"form": form})

# Borrar Producto


def delete_product(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.ProductoCategoriaa.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:02lista_producto")
    return render(request, "producto/05delete_producto.html", {"object": query})
