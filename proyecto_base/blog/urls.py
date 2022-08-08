from django.urls import path
from .views import BlogView

app_name='blog'

urlpatterns = [
    path('blog', BlogView.as_view(template_name='blog.html'), name='blog'),
    ]