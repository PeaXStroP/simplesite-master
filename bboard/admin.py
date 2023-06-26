from django.contrib import admin
from .models import Bboard, Category


class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'category', 'created_at', 'is_published')
    list_display_links = ('title', 'content', 'category')
    search_fields = ('title', 'content', 'price', 'category')
    list_editable = ('is_published', )
    list_filter = ('author', 'category', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Bboard, BboardAdmin)
admin.site.register(Category, CategoryAdmin)
