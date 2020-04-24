from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import GalleryItem, Category

class Gallery(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 25


# Register your models here.
admin.site.register(GalleryItem, Gallery)
admin.site.register(Category)
