from django.shortcuts import render
from homepage.models import SlideShowItem, GalleryCategory


# Create your views here.
def homepage(request):
    slideshow = SlideShowItem.objects.all()
    categories = GalleryCategory.objects.all()
    context = {
        'slideshow': slideshow,
        'categories': categories,
        'instagram_profile_name': 'lesleyannegreene',
    }
    return render(request, 'index.html', context)
