from django.contrib import admin

from .models import Buzz

@admin.register(Buzz)
class BuzzAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'status', 'publish', 'updated']
    list_filter = ['status', 'slug', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
