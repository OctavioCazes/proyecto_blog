from calendar import c
from io import UnsupportedOperation
from django import forms
from .models import Usuario 
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "username", "password1", "password2"]
       
