
from unicodedata import category
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
# Create your views here.
from . import models
from . import forms

#def home(request):
    #contexto = {"app": "customer"}
    #return render(request, "customer/index.html", contexto)

# Lista Cliente
def list_customer(request):
    categorias = models.Customer.objects.all()
    context = {"objects_list": categorias}
    return render(request, "customer/02lista_customer.html", context)

# class ProductoCategoriaaList (ListView):
    # model = models.ProductoCategoriaa

# Crear Cliente
def create_customer(request):
    if request.method == "POST":
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = forms.CustomerForm()
    return render(request, "customer/01crear_customer.html", {"form": form})

# Detalles Cliente
def detail_customer(request, pk):
    query = models.Customer.objects.get(id=pk)
    return render(request, "customer/03detail_customer.html", {"object": query})

# Actualizar Customer


def update_customer(request, pk):
    query = models.Customer.objects.get(id=pk)
    if request.method == "POST":
        form = forms.CustomerForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = forms.CustomerForm(instance=query)
    return render(request, "customer/01crear_customer.html", {"form": form})

# Borrar Cliente
def delete_customer(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Customer.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:02lista_producto")
    return render(request, "customer/05delete_customer.html", {"object": query})
