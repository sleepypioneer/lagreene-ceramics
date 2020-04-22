from django.shortcuts import render
from .models import GalleryItem, Tag

# Create your views here.
def gallery(request):
    gallery = GalleryItem.objects.all()
    tags = Tag.objects.all().order_by('word')
    context = {
        'gallery': gallery,
        'categories': tags,
    }
    return render(request, 'gallery.html', context)
