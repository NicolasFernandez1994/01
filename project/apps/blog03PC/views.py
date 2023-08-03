from django.shortcuts import render

def home(request):
    contexto = {"app": "blog03PC"}
    return render(request, "blog03PC/index.html", contexto)
