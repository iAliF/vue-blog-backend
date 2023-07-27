from django.contrib import admin

from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'slug')
    search_help_text = "Enter title or slug to search"
    list_display = ('author', 'title', 'created_at', 'updated_at')
    list_filter = ('author__username',)
    sortable_by = ('created_at', 'updated_at')
    prepopulated_fields = {
        'slug': ('title',)
    }
