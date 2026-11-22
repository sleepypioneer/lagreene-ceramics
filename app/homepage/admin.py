from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SlideShowItem, NewsItem

class SlideShowAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_per_page = 10

class NewsItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'itemOrder')
    list_display_links = ('title',)
    search_fields = ['title', 'main_text']
    list_per_page = 10
    fieldsets = (
        ('Content', {
            'fields': ('title', 'main_text')
        }),
        ('Media & Link', {
            'fields': ('image', 'link'),
            'classes': ('collapse',),
            'description': 'Image and link are optional'
        }),
        ('Ordering', {
            'fields': ('itemOrder',)
        }),
    )

# Register your models here.
admin.site.register(SlideShowItem, SlideShowAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
