
from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from usuarios.form_usuarios import UsuarioForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login2
from django.contrib import messages




from usuarios.models import Usuario


def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name, {})

def login(request): 
    data = {
        'form' : Usuario
    }
    if request.method == 'POST':
        formulario = Usuario(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password"]
            user =  username, password
            login2(request, user)
            messages.success(request, "Te has logeado exitosamente")
            return redirect('inicio')
    template_name = 'accounts/login.html'
    return render(request, template_name, data)

def registrarse(request):
    data = {
        'form' : UsuarioForm
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password"])
            login2(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect('inicio')
    return render(request, 'templates_usuarios/crear_usuario.html', data)

def noticias(request):
    template_name = 'noticias.html'
    return render(request, template_name)

def quienes(request):
    template_name = 'quienes.html'
    return render(request, template_name)

def mision(request):
    template_name = 'mision.html'
    return render(request, template_name)

def vision(request):
    template_name = 'vision.html'
    return render(request, template_name)

def contacto(request):
    template_name = 'contacto.html'
    return render(request, template_name)

def eventos(request):
    template_name = 'eventos.html'
    return render(request, template_name)

def recursos(request):
    template_name = 'recursos.html'
    return render(request, template_name)
