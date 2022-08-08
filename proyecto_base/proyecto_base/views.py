
from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from usuarios.form_usuarios import UsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate
from usuarios.models import Usuario
from blog.models import Post


def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name, {})

def login(request): 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user, backend=None)
    template_name = 'accounts/login.html'
    return render(request, template_name)

def registrarse(request):
    data = {
        'form' : UsuarioForm
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            auth_login(request, user)
            messages.success(request,"Te has registrado exitosamente")
            return redirect('inicio')
    return render(request, 'templates_usuarios/crear_usuario.html', data)

def noticias(request):
    post ={
        'post':Post.postobjects.all()
    } 
    template_name = 'noticias.html'
    return render(request, template_name, post)

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
