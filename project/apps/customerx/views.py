from unicodedata import category
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
# Create your views here.
from . import models
from . import forms

# Pagina principal
def home(request):
     contexto = {"app": "customerx"}
     return render(request, "customerx/index.html", contexto)

# Lista Cliente


def list_customerx(request):
    categorias = models.Customerx.objects.all()
    context = {"objects_list": categorias}
    return render(request, "customerx/02lista_customerx.html", context)

# Crear Cliente


def create_customerx(request):
    if request.method == "POST":
        form = forms.CustomerxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customerx:home")
    else:
        form = forms.CustomerxForm()
    return render(request, "customerx/01crear_customerx.html", {"form": form})

# Detalles Cliente


def detail_customerx(request, pk):
    query = models.Customerx.objects.get(id=pk)
    return render(request, "customerx/03detail_customerx.html", {"object": query})

# Actualizar Customer


def update_customerx(request, pk):
    query = models.Customerx.objects.get(id=pk)
    if request.method == "POST":
        form = forms.CustomerxForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("customerx:home")
    else:
        form = forms.CustomerxForm(instance=query)
    return render(request, "customerx/01crear_customerx.html", {"form": form})

# Borrar Cliente

def delete_customerx(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Customerx.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("customerx:02lista_customerx")
    return render(request, "customerx/05delete_customerx.html", {"object": query})
