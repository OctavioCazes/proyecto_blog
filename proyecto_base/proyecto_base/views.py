import re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name, {})

def login(request):
    template_name = 'accounts/login.html'
    return render(request, template_name)

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
