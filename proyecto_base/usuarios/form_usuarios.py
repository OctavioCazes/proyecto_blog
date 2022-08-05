from io import UnsupportedOperation
from django import forms
from .models import Usuario 
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = 'username', 'password'


class CreacionUsuario(UserCreationForm):
    pass