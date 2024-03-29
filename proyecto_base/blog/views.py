
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ComentarioForm
from .models import Comentario, Post
from core.mixins import SuperUserRequiredMixin
from django.urls import reverse
from blog.forms import PostForm





class ComentarioView(LoginRequiredMixin ,CreateView):
	template_name = 'templates_blog/comentario.html'
	model = Comentario
	form_class = ComentarioForm

	def form_valid(self, form):
		f = form.save(commit=False)
		f.name = self.request.user
		return super(ComentarioView, self).form_valid(form)
	

	
	def get_success_url(self, **kwargs):
		return reverse('noticias')

class BlogView(TemplateView):
	template_name='templates_blog/blog.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["posts"] = Post.postobjects.all()
		context["comentario"] = Comentario.objects.all()
		return context

class CrearNoticias(SuperUserRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'templates_blog/crear.html'
	
	def get_success_url(self, **kwargs):
		return reverse('noticias')

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

   