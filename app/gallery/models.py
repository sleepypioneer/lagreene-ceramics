from django.db import models

class Tag(models.Model):
    word = models.CharField(max_length=35)

    def __unicode__(self):
        return self.word


# Create your models here.
class GalleryItem(models.Model):
    image = models.ImageField(upload_to="img/gallery")
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    categories = models.ManyToManyField(Tag, related_name='photos')
    archive = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def class_string(self):
        class_string = ""
        for tag in self.categories.all():
            class_string += str(tag.word) + " "
        return class_string

    class Meta(object):
        ordering = ['my_order']
