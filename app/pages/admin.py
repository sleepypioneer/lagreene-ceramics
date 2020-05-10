from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Link, Stockist, Venue

class LinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 15

class StockistAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'stockist_venue']
    list_display_links = ['title']
    list_filter = ['end_date', 'venue']
    search_fields = ['title']

    def year(self, obj):
        return obj.end_date.year

    def stockist_venue(self, obj):
        return obj.venue.name

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


# Register your models here.
admin.site.register(Link, LinkAdmin)
admin.site.register(Stockist, StockistAdmin)
admin.site.register(Venue, VenueAdmin)
