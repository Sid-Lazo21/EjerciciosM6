from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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



@login_required
def vista_restringida(request):
    # Tu lógica de vista aquí
    return render(request, 'authenticated/home.html')




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio después de iniciar sesión
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'authenticated/home.html', {'username': request.user.username})



def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('authenticated/home.html')  # Redirige a la página de inicio
    else:
        form = UserCreationForm()
    return render(request, 'registro-usuario.html', {'form': form})










