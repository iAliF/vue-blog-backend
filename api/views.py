from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Article
from .serializers import ArticleSerializers


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = "slug"
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "slug")
    ordering_fields = ("title", "created_at")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
