from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views.generic import ListView

from .forms import CustomerForm

# Create your views here.
from .models import Customer


def home(request):
    customer_registros = Customer.objects.all()
    contexto = {"customer": customer_registros}
    # return render(request, "index.html", {"customer": customer_registros})
    return render(request, "customer/index.html", contexto)


def crear_customers(request):
    from datetime import date

    c1 = Customer(nombre="Almendra", apellido="Ruiseñor",
                  nacimiento=date(2015, 1, 1), dni="12345678", numero_cliente=1)
    c2 = Customer(nombre="Giordana", apellido="Tapello",
                  nacimiento=date(2005, 2, 2), dni="12335678", numero_cliente=2)
    c3 = Customer(nombre="Macarena", apellido="Lito",
                  nacimiento=date(1990, 1, 1), dni="12344678", numero_cliente=3)
    c4 = Customer(nombre="Jhiordana", apellido="Perez",
                  nacimiento=date(2005, 1, 1), dni="12346678", numero_cliente=5)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("customer:home")


def crear_customer(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer:home")
    else:  # request.method == "GET"
        form = CustomerForm()
    return render(request, "customer/crear.html", {"form": form})


def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "dana"
    customer_nombre = Customer.objects.filter(nombre__contains="dana")

    # Nacimientos  mayores a 2000
    customer_nacimiento = Customer.objects.filter(
        nacimiento__gt=date(2000, 1, 1))

    # Dni
    customer_dni = Customer.objects.filter(dni_contains="123")

    # Numero de customer
    customer_numero_customer = Customer.objects.filter(numero_customer__gt=1)

    contexto = {
        "customer_nombre": customer_nombre,
        "customer_nacimiento": customer_nacimiento,
        "customer_dni": customer_dni,
        "customer_numero_customer": customer_numero_customer,
    }
    return render(request, "customer/search.html", contexto)
