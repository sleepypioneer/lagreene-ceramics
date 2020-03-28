from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('gallerylist/',
         views.gallery,
         name='gallery'),
    path('photolist/',
         views.gallery,
         name='gallery'),
]
