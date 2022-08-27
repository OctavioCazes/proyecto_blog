from distutils.command.install_egg_info import to_filename
from django.contrib.auth.models import User
from email.policy import default
from random import choices
from django.db import models
from django.utils import timezone



class Categorias(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #Clase dentro de otra clase,vamos a usar para buscar y mostrar los articulos en pantalla publicados
    class PostObjects(models.Manager):
        def get_queryser(self):
            return super().get_queryset().filter(estado='published', categoria = '1')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    # vinculamos el modelo, cuando borramos categorias, pretejemos, 
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, default=1)
    imagenes = models.ImageField(upload_to="imagenes", null=True, blank=True)
    titulo_not = models.CharField(max_length=255)
    #breve descripcion del articulo
    excerpt = models.TextField(null=True)
    contenido_no = models.TextField(null=True)
    # slug para poder acceder al url, el slag es unico 
    slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    #estado publicado o en borrador
    estado = models.CharField(max_length=10, choices=options, default='draft')
    objet = models.Manager()
    postobjects = PostObjects()


    class Meta():
        ordering = ('-published',)
    
    def __str__(self):
        return self.titulo_not 




class Comentario(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta():
        ordering = ('publish',)

    def _str_(self):
        return f"Comentado por {self.name}"




