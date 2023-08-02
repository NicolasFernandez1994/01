from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {"app": "productoscompra"}
    return render(request, "productoscompra/index.html", contexto) #corregir