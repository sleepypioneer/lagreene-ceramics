from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SlideShowItem

class SlideShowAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_per_page = 10


# Register your models here.
admin.site.register(SlideShowItem, SlideShowAdmin)
