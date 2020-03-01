from django.shortcuts import render
from homepage.models import SlideShowItem


# Create your views here.
def homepage(request):
    slideshow = SlideShowItem.objects.all()
    context = {
        'slideshow': slideshow,
        'instagram_profile_name': 'lesleyannegreene',
    }
    return render(request, 'homepage/index.html', context)
