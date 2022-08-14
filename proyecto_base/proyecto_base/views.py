
import imp
from re import template
from django.urls import reverse
from email import message
from django.shortcuts import redirect, render
from usuarios.form_usuarios import UsuarioForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate
from blog.models import Post
from django.views.generic.edit import CreateView, UpdateView
from blog.forms import PostForm
from core.mixins import SuperUserRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name, {})

def login(request): 
        data = {
        'form' : UsuarioForm
        }
        if request.method == 'POST':
            password = request.POST["password", None]
            usuario = request.POST["username", None]
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                auth_login(request,user, data)

        template_name = 'accounts/login.html'
        return render(request, template_name, data)

def get_success_url(self, **kwargs):
        return reverse('inicio')


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

class CrearNoticias(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crear.html'
    
    def get_success_url(self, **kwargs):
        return reverse('inicio')
    

# def crear(request):
#    template_name = 'crear.html'
#    return render(request, template_name)

#class Actualizar(UpdateView):
#    template_name="actualizar.html"
#    model=Post
#    form_class = PostForm

#    def get_success_url(self, **kwargs):
#

@login_required
def editar(request,id):
    post = Post.postobjects.get(id=id)
    formulario = PostForm(request.POST or None, request.FILES or None, instance=post)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('noticias')
    return render(request, 'actualizar.html', {'formulario':formulario})

@login_required
def eliminar(request, id):
    post = Post.postobjects.get(id=id)
    post.delete()
    return redirect('noticias')