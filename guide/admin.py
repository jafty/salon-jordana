from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'layout_type', 'created_at')
    list_filter = ('is_featured', 'layout_type', 'category', 'created_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
