from django.shortcuts import render
from .models import GalleryItem, Tag

# Create your views here.
def gallery(request):
    gallery = GalleryItem.objects.all()
    categories = Tag.objects.all()
    context = {
        'gallery': gallery,
        'categories': categories,
    }
    return render(request, 'gallery.html', context)
