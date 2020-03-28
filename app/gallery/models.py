from django.db import models

# Create your models here.
class GalleryItem(models.Model):
    image = models.ImageField(upload_to="img/gallery")
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
