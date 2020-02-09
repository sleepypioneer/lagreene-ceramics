from django.shortcuts import render
from homepage.models import SlideShowItem, GalleryCategory


# Create your views here.
def index(request):
    slideshow = SlideShowItem.objects.all()
    categories = GalleryCategory.objects.all()
    context = {
        'slideshow': slideshow,
        'categories': categories,

    }
    return render(request, 'homepage.html', context)
