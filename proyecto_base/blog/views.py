from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class BlogView(TemplateView):
    template_name='blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.all()
        return context

"""def blog(request):
   context= {
    'form': Post
   }
   template_name = 'templates/blog.html'
   return render(request, template_name,context)"""
   