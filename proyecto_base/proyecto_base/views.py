
from django.urls import reverse
from django.shortcuts import redirect, render
from usuarios.form_usuarios import UsuarioForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate
from blog.models import Post
from django.views.generic import TemplateView, ListView
from blog.filters import CategoriasFilter

def inicio(request):
	template_name = 'inicio.html'
	return render(request, template_name, {})

def login(request):
	template_name = 'accounts/login.html' 
	data = {
	'form' : UsuarioForm
	}
	if request.method == 'POST':
		password = request.POST["password", None]
		usuario = request.POST["username", None]
		user = authenticate(request, username=usuario, password1=password)
		if user is not None:
			auth_login(request,user)
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
	filtro = Post.postobjects.all()
	filtro_post = CategoriasFilter(request.GET, queryset=filtro)
	post ={
		'post':Post.postobjects.all(),
		'filtro': filtro_post
		} 
	template_name = 'noticias.html'
	return render(request, template_name, post)

"""
class Noticias(ListView):
	template_name='noticias.html'
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["posts"] = Post.postobjects.all()
		context["filtro"] = CategoriasFilter(self.request.GET, queryset=self.get_queryset())
		return context
"""

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

