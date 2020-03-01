from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("about", views.about, name="about"),
    path("exhibitions", views.exhibitions, name="exhibitions"),
    path("cv", views.cv, name="cv"),
    path("links", views.links, name="links"),
    path("contact", views.contact, name="contact"),
]
