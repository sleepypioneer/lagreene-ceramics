from django.shortcuts import render

def about(request):
    context = {
    }
    return render(request, 'about.html', context)

def exhibitions(request):
    context = {
    }
    return render(request, 'exhibitions.html', context)

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
