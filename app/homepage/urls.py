from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('', TemplateView.as_view(template_name='instagram.html', extra_context={
        "instagram_profile_name": "lesleyannegreene"
    })),
]