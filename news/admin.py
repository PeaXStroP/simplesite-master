from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'category', 'publish_date', 'update_date', 'is_published')
    list_display_links = ('title', 'content', 'category')
    search_fields = ('title', 'content', 'category')
    list_editable = ('is_published', )
    list_filter = ('author', 'category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
