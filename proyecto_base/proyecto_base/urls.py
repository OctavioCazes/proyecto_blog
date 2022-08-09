"""proyecto_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('account/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cerrar-sesion', auth_views.logout_then_login, name="logout" ),
    path('registrarse', views.registrarse, name='registrarse'),
    path('noticias/', views.noticias, name='noticias'),
    path('quienes/', views.quienes, name='quienes'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('contacto/', views.contacto, name='contacto'),
    path('eventos/', views.eventos, name='eventos'),
    path('recursos/', views.recursos, name='recursos'),
    path('blog/', include('blog.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
