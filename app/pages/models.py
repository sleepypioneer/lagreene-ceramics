from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=100)
    