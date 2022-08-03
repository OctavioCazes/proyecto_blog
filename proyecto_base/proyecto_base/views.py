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
