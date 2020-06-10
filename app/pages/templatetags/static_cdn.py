from django import template
from django.template.defaultfilters import stringfilter
from django.templatetags.static import static
from django.conf import settings

register = template.Library()

@register.simple_tag
def static_cdn(url):
    if settings.CDN_ENABLED:
        url = static(url).replace(
            settings.AWS_S3_CUSTOM_DOMAIN,
            settings.AWS_S3_CDN_DOMAIN).replace(
            '/static/',
            '/')
        return url
    else:
        return static(url)
