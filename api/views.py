from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Article
from .serializers import ArticleSerializers


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = "slug"
    filter_backends = (SearchFilter,)
    search_fields = ("title", "slug")
