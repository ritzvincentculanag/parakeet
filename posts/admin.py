from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['author','content','created','status']
    list_filter = ['author','status']
    search_fields = ['author']
    ordering = ['status','created']
    date_hierarchy = 'created'
    show_facets = admin.ShowFacets.ALWAYS
