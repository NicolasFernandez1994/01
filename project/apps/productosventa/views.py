from django.shortcuts import render

def home(request):
    contexto = {"app": "productosventa"}
    return render(request, "productosventa/index.html", contexto) #corregir