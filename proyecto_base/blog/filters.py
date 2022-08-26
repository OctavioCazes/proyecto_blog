import django_filters
from .models import Post
class CategoriasFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Post
        #fields = ['published', 'categoria']
        fields = {'categoria': ['exact']}
