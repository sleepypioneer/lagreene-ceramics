from django.db import models

class SlideShowItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img/slideshowIndex")


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    image = models.ImageField(upload_to="img/categories")
