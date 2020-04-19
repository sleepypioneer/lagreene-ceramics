from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Link

class LinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 15


# Register your models here.
admin.site.register(Link, LinkAdmin)
