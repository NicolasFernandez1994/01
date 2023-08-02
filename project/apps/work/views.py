from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {"app": "work"}
    return render(request, "work/index.html", contexto) #corregir