from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.

def index(request):
    return HttpResponse("<H1> ESTA ES LA PAGINA DE INICIO DE MI APLICATIVO </H1>")



def user_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'user_list.html', {'usuarios': usuarios})


def landing(request):
    return render(request, 'landing.html')  # Cambia 'landing.html' por el nombre de tu plantilla






