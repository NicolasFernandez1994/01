from django.shortcuts import render

def home(request):
    contexto = {"app": "blog02EH"}
    return render(request, "blog02EH/index.html", contexto)
