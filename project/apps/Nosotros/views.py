from django.shortcuts import render

# Create your views here.


def home(request):
    contexto = {"app": "Nosotros"}
    return render(request, "Nosotros/index.html", contexto)
