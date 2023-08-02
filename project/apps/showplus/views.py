from django.shortcuts import render

def home(request):
    contexto = {"app": "showplus"}
    return render(request, "showplus/index.html", contexto) #corregir
