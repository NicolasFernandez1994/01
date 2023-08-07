from django.shortcuts import render, redirect
from .forms import ShowplusForm
from unicodedata import category
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
# Create your views here.
from . import models
from . import forms

# Pagina principal


def home(request):
    contexto = {"app": "showplus"}
    return render(request, "showplus/index.html", contexto)  # corregir

# AGREGAR PRODUCTO


def agregar_showplus(request):
    if request.method == 'POST':
        form = ShowplusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showplus:agregar')
    else:
        form = ShowplusForm()
    return render(request, 'showplus/agregar_showplus.html', {'form': form})

# LISTA SHOWPLUS


def list_showplus(request):
    categorias = models.Showplus.objects.all()
    context = {"objects_list": categorias}
    return render(request, "showplus/02lista_showplus.html", context)

# Crear Showplus


def create_showplus(request):
    if request.method == "POST":
        form = forms.ShowplusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("showplus:home")
    else:
        form = forms.ShowplusForm()
    return render(request, "showplus/01agregar_showplus.html", {"form": form})

# Detalles Showplus


def detail_showplus(request, pk):
    query = models.Showplus.objects.get(id=pk)
    return render(request, "showplus/03detail_showplus.html", {"object": query})

# Actualizar Showplus


def update_showplus(request, pk):
    query = models.Showplus.objects.get(id=pk)
    if request.method == "POST":
        form = forms.ShowplusForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("showplus:home")
    else:
        form = forms.ShowplusForm(instance=query)
    return render(request, "showplus/01agregar_showplus.html", {"form": form})

# Borrar Showplus

def delete_showplus(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Showplus.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("showplus:02lista_showplus")
    return render(request, "showplus/05delete_showplus.html", {"object": query})
