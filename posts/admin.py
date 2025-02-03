from django.contrib import admin

from .models import Post, Like


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created', 'status']
    list_filter = ['author', 'status']
    search_fields = ['content']
    ordering = ['status', 'created']
    date_hierarchy = 'created'
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['post']
    search_fields = ['post__content']
    date_hierarchy = 'created'
