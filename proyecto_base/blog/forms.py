from dataclasses import fields
from django import forms 
from blog.models import Post, Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["categoria", "titulo_not", "imagenes", "excerpt", "contenido_no", "published", "estado"]



class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ["content", "post"]
