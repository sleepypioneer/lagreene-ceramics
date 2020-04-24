from django.shortcuts import render
from pages.models import Link, Show, Venue
from django.utils import timezone

def today():
    return timezone.localtime(timezone.now()).date()

def about(request):
    context = {
    }
    return render(request, 'about.html', context)

def stockists(request):
    context = {
        'current_shows': Show.objects.filter(end_date__gte=timezone.now()).order_by('-end_date'),
        'past_shows': Show.objects.filter(end_date__lt=timezone.now()).order_by('-end_date'),
        'venues': Venue.objects.all().order_by('name'),
        'exhibition_years': sorted(Show.objects.all().values_list('end_date__year', flat=True).distinct()),
    }
    return render(request, 'stockists.html', context)

def cv(request):
    context = {
    }
    return render(request, 'cv.html', context)

def links(request):
    links = Link.objects.all()
    context = {
        'links': links,
    }
    return render(request, 'links.html', context)

def contact(request):
    context = {
    }
    return render(request, 'contact.html', context)
