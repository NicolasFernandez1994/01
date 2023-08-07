from django.shortcuts import render, redirect
from .forms import WorkForm
from unicodedata import category
from django.http import HttpRequest, HttpResponse
# Create your views here.
from . import models
from . import forms

# Pagina principal


def home(request):
    contexto = {"app": "work"}
    return render(request, "work/index.html", contexto)

# Agregar Work


def agregar_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('work:agregar')
    else:
        form = WorkForm()
    return render(request, 'work/01agregar_work.html', {'form': form})

# Lista Work


def list_work(request):
    categorias = models.Work.objects.all()
    context = {"objects_list": categorias}
    return render(request, "work/02lista_work.html", context)

# Crear Work


def create_work(request):
    if request.method == "POST":
        form = forms.WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work:home")
    else:
        form = forms.WorkForm()
    return render(request, "work/01agregar_work.html", {"form": form})

# Detalles Work


def detail_work(request, pk):
    query = models.Work.objects.get(id=pk)
    return render(request, "work/03detail_work.html", {"object": query})

# Actualizar Work


def update_work(request, pk):
    query = models.Work.objects.get(id=pk)
    if request.method == "POST":
        form = forms.WorkForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("work:home")
    else:
        form = forms.WorkForm(instance=query)
    return render(request, "work/01agregar_work.html", {"form": form})

# Borrar Work


def delete_work(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Work.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("work:02lista_work")
    return render(request, "work/05delete_work.html", {"object": query})
