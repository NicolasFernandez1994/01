from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {"app": "customer"}
    return render(request, "customer/index.html", contexto)