from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import GalleryItem, Category

class Gallery(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'item_categories']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 25

    def item_categories(self, obj):
        return ", ".join([p.name for p in obj.categories.all()])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


# Register your models here.
admin.site.register(GalleryItem, Gallery)
admin.site.register(Category, CategoryAdmin)
