from django.shortcuts import render
from pages.models import Link, Stockist, Venue
from django.utils import timezone

def about(request):
    context = {
    }
    return render(request, 'about.html', context)

def stockists(request):
    context = {
        'current_stockists': Stockist.objects.filter(
            end_date__gte=timezone.now()).order_by('-end_date'),
        'past_stockists': Stockist.objects.filter(
            end_date__lt=timezone.now()).order_by('-end_date'),
        'venues': Venue.objects.all().order_by('name'),
        'exhibition_years': set(sorted(
            Stockist.objects.filter(end_date__lt=timezone.now())
                .values_list(
                    'end_date__year',
                    flat=True),
            reverse=True
        )),
    }
    return render(request, 'stockists.html', context)

def cv(request):
    return render(request, 'cv.html')

def links(request):
    links = Link.objects.all()
    context = {
        'links': links,
    }
    return render(request, 'links.html', context)

def contact(request):
    return render(request, 'contact.html')

def custom_page_not_found_view(request, exception):
    return render(request, 'error_pages/404.html', status=404)

def custom_server_error_view(request):
    return render(request, 'error_pages/500.html', status=500)

def custom_bad_request_view(request, exception):
    return render(request, 'error_pages/400.html', status=400)

def custom_permission_denied_view(request, exception):
    return render(request, 'error_pages/403.html', status=403)
