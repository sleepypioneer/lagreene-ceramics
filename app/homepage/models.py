from django.db import models

class SlideShowItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img/slideshowIndex")
    itemOrder = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['itemOrder']

class Announcement(models.Model):
    subject = models.CharField(max_length=75, primary_key=True)
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to="img/announcement")
    link = models.URLField(max_length=100)
    publish_date = models.DateTimeField()
    end_date = models.DateTimeField()
