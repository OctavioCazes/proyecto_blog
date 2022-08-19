from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import Post
from core.mixins import SuperUserRequiredMixin
from usuarios.form_usuarios import UsuarioForm
from django.urls import reverse
from blog.forms import PostForm

# Create your views here.
class BlogView(TemplateView):
    template_name='templates_blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.all()
        return context

class CrearNoticias(SuperUserRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'templates_blog/crear.html'
    
    def get_success_url(self, **kwargs):
        return reverse('inicio')

class Actualizar(SuperUserRequiredMixin, UpdateView):
    template_name="templates_blog/actualizar.html"
    model=Post
    form_class = PostForm

    def get_success_url(self, **kwargs):
        return reverse ('noticias') 

class Eliminar(SuperUserRequiredMixin ,DeleteView):
    model=Post
    def get_success_url(self, **kwargs):
        return reverse ('inicio') 
    template_name = "templates_blog/eliminar.html"

   