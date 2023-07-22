from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {"app": "faq"}
    return render(request, "faq/index.html", contexto)
