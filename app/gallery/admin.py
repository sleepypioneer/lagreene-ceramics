from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import GalleryItem, Category

def archive_gallery_item(modeladmin, request, gallery_items):
    for gallery_item in gallery_items:
        gallery_item.archive = True
        gallery_item.save()


archive_gallery_item.short_description = "Archive gallery item/s"

class Gallery(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'item_categories', 'item_archived', 'in_artists_selection']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 25
    list_filter = ['categories']
    actions = [archive_gallery_item, ]

    def item_categories(self, obj):
        return ", ".join([p.name for p in obj.categories.all()])

    def item_archived(self, obj):
        if obj.archive:
            return "archived"

    def in_artists_selection(self, obj):
        if obj.artists_selection:
            return "True"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

    search_fields = ['name']


# Register your models here.
admin.site.register(GalleryItem, Gallery)
admin.site.register(Category, CategoryAdmin)
