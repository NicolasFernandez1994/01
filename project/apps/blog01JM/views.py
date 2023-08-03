from django.shortcuts import render


def home(request):
    contexto = {"app": "blog01JM"}
    return render(request, "blog01JM/index.html", contexto)
