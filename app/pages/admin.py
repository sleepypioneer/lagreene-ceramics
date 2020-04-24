from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Link, Stockist, Venue

class LinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 15

class StockistAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


# Register your models here.
admin.site.register(Link, LinkAdmin)
admin.site.register(Stockist, StockistAdmin)
admin.site.register(Venue, VenueAdmin)
