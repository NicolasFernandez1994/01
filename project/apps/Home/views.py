from django.contrib.admin.views.decorators import staff_member_required
from audioop import reverse
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
from . import forms


def home(request):
    return render(request, "Home/index.html")

#! LOGIN


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje": "Sesion iniciada correctamente"})
    else:
        form = AuthenticationForm()
    return render(request, "Home/login.html", {"form": form})

#! REGISTER


@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            return render(request, "Home/index.html", {"mensaje": "Usuario Creado correctamente"})
    else:
        form = AuthenticationForm()
    return render(request, "Home/register.html", {"form": form})
