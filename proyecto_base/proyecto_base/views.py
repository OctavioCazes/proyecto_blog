from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from usuarios.models import Usuario


def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name, {})

def login(request):
    template_name = 'accounts/login.html'
    return render(request, template_name)

def noticias(request):
    template_name = 'noticias.html'
    return render(request, template_name)
