from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=100)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
