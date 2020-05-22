from django.db import models
import datetime

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['name']


# Create your models here.
class GalleryItem(models.Model):
    image = models.ImageField(upload_to="img/gallery")
    title = models.CharField(max_length=75, primary_key=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='photos')
    archive = models.BooleanField()
    artists_selection = models.BooleanField()
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def class_string(self):
        class_string = ""
        for category in self.categories.all():
            class_string += str(category.name).lower().replace(" ", "_") + " "
        if self.archive:
            class_string += ' archive'
        if self.artists_selection:
            class_string += 'artists_selection glightbox'
        else:
            class_string += ' d-none'

        return class_string

    def year_created(self):
        YEAR_CHOICES = []
        for r in range(1980, (datetime.datetime.now().year+1)):
            YEAR_CHOICES.append((r, r))
        return YEAR_CHOICES

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['my_order']
