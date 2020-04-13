from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=75)
    link = models.URLField(max_length=100)
    itemOrder = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['itemOrder']
