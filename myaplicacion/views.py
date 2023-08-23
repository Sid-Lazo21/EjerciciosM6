from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def index(request):
    return HttpResponse("<H1> ESTA ES LA PAGINA DE INICIO DE MI APLICATIVO </H1>")

def user_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'user_list.html', {'usuarios': usuarios})

def landing(request):
    return render(request, 'landing.html')  # Cambia 'landing.html' por el nombre de tu plantilla


def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Página de éxito de registro
    else:
        form = UsuarioForm()
    return render(request, 'registro-usuario.html', {'form': form})


def registro_exitoso(request):
    return render(request, 'registro-exitoso.html')









