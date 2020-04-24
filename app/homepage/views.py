from django.shortcuts import render
from homepage.models import SlideShowItem, Announcement


# Create your views here.
def homepage(request):
    slideshow = SlideShowItem.objects.all()
    announcements = Announcement.objects.all()
    context = {
        'slideshow': slideshow,
        'announcements': announcements,
        'instagram_profile_name': 'lesleyannegreene',
    }
    return render(request, 'homepage/index.html', context)
