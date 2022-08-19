from django.urls import path

from .views import *

app_name='blog'

urlpatterns = [
    path('<int:id>', BlogView.as_view(template_name='templates_blog/blog.html'), name='blog'),
    path('crear', CrearNoticias.as_view(), name='crear'),
    path('actualizar/<str:slug>/', Actualizar.as_view(), name='actualizar'),    
    path('eliminar/<str:slug>/', Eliminar.as_view(), name='eliminar'),
]