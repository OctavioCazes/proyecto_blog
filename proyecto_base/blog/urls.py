from django.urls import path

from .views import *

app_name='blog'

urlpatterns = [
    path('<int:id>', BlogView.as_view(template_name='templates_blog/blog.html'), name='blog'),
    path('crear', CrearNoticias.as_view(), name='crear'),
    path('comentar/<int:id>', ComentarioView.as_view(), name='comentar'),
    path('actualizar/<int:pk>/', Actualizar.as_view(), name='actualizar'),    
    path('eliminar/<int:pk>/', Eliminar.as_view(), name='eliminar'),
    path('filtro', categoria_list, name = 'filtro')
]