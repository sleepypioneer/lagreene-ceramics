from django.shortcuts import render
from .models import GalleryItem, Category

# Create your views here.
def gallery(request):
    gallery = GalleryItem.objects.all()
    categories = Category.objects.all().order_by('word')
    context = {
        'gallery': gallery,
        'categories': categories,
    }
    return render(request, 'gallery.html', context)
