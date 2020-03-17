from django.shortcuts import render
from .models import GalleryItem

# Create your views here.
def gallery(request):
    gallery = GalleryItem.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery.html', context)
