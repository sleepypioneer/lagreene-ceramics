from django.db.models import F
from django.shortcuts import render
from django.utils import timezone

from homepage.models import SlideShowItem, Announcement
from pages.models import Stockist


# Create your views here.
def homepage(request):
    slideshow = SlideShowItem.objects.all()
    announcements = Announcement.objects.all()
    upcoming_stockist = Stockist.objects.filter(
        end_date__gte=timezone.localdate()
    ).order_by(F('start_date').asc(nulls_last=True)).first()
    context = {
        'slideshow': slideshow,
        'announcements': announcements,
        'instagram_profile_name': 'lesleyannegreene',
        'upcoming_stockist': upcoming_stockist,
    }
    return render(request, 'homepage/index.html', context)
