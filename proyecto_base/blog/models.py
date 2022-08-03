from datetime import datetime, timezone
from ssl import Options
from django.db import models

"""
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
        title = models.CharField(max_length=255)
        excerpt = models.TextField(null=True)
        content = models.TextField()
        slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
        published = models.DateTimeField(default=datetime.now())
        #author = models.ForeignKey(auth_user, on_delete=models.CASCADE, related_name='blog_posts')
        status = models.CharField(max_length=10, choices=Options, default='draft')

"""