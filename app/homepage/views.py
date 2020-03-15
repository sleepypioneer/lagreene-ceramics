from django.shortcuts import render
from homepage.models import SlideShowItem
from news.models import Show


# Create your views here.
def homepage(request):
    slideshow = SlideShowItem.objects.all()
    shows = Show.objects.all()
    context = {
        'slideshow': slideshow,
        'curent_shows': shows,
        'instagram_profile_name': 'lesleyannegreene',
    }
    return render(request, 'homepage/index.html', context)
