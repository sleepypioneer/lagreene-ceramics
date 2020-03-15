from django.shortcuts import render
from news.models import Show

def about(request):
    context = {
    }
    return render(request, 'about.html', context)

def stockists(request):
    shows = Show.objects.all()
    context = {
        'curent_shows': shows,
    }
    return render(request, 'stockists.html', context)

def cv(request):
    context = {
    }
    return render(request, 'cv.html', context)

def links(request):
    context = {
    }
    return render(request, 'links.html', context)

def contact(request):
    context = {
    }
    return render(request, 'contact.html', context)
