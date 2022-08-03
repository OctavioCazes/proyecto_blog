from re import template
from django.shortcuts import render



def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name, {})
"""
def login(request):
    template_name = 'login.html'
    return render(request, template_name)
"""
def noticias(request):
    template_name = 'noticias.html'
    return render(request, template_name)
