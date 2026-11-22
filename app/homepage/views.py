from django.shortcuts import render
from django.utils import timezone

from homepage.models import SlideShowItem, Announcement, NewsItem


# Create your views here.
def homepage(request):
    slideshow = SlideShowItem.objects.all()
    announcements = Announcement.objects.all()
    news_items = NewsItem.objects.all()
    context = {
        'slideshow': slideshow,
        'announcements': announcements,
        'instagram_profile_name': 'lesleyannegreene',
        'news_items': news_items,
    }
    return render(request, 'homepage/index.html', context)
