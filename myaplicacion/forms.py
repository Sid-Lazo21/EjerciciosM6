from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password']  # Agrega los campos necesarios

class LoginForm(AuthenticationForm):
    # Puedes personalizar el formulario aquí si lo deseas
    pass




