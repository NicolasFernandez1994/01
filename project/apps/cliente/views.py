from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import ClienteForm

# Create your views here.
from .models import Cliente


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)


def crear_clientes(request):
    from datetime import date

    c1 = Cliente(nombre="Almendra", apellido="Ruiseñor",
                 nacimiento=date(2015, 1, 1), dni="12345678", numero_cliente = 1)
    c2 = Cliente(nombre="Giordana", apellido="Tapello",
                 nacimiento=date(2005, 2, 2), dni="12335678", numero_cliente = 2)
    c3 = Cliente(nombre="Macarena", apellido="Lito",
                 nacimiento=date(1990, 1, 1), dni="12344678", numero_cliente = 3)
    c4 = Cliente(nombre="Jhiordana", apellido="Perez",
                 nacimiento=date(2005, 1, 1), dni="12346678", numero_cliente = 5)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:home")


def crear_cliente(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})


def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "dana"
    cliente_nombre = Cliente.objects.filter(nombre__contains="dana")

    # Nacimientos  mayores a 2000
    cliente_nacimiento = Cliente.objects.filter(
        nacimiento__gt=date(2000, 1, 1))

    # Dni
    cliente_dni = Cliente.objects.filter(dni_contains="123")

    # Numero de cliente
    cliente_numero_cliente = Cliente.objects.filter(numero_cliente__gt=1)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_nacimiento": cliente_nacimiento,
        "clientes_dni" : cliente_dni,
        "clientes_numero_cliente": cliente_numero_cliente,
    }
    return render(request, "cliente/search.html", contexto)
