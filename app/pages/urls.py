from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("about", views.about, name="about"),
    path("stockists", views.stockists, name="stockists"),
    path("cv", views.cv, name="cv"),
    path("links", views.links, name="links"),
    path("contact", views.contact, name="contact"),
]
