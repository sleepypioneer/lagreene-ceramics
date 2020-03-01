from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=75)
    address = models.ForeignKey('Address')
    link = models.URLField(max_length=100)
    start = models.DateTimeField(auto_now=True, auto_now_add=True)
    end = models.DateTimeField()
class Address(models.Model):
    number = models.PositiveIntegerField(_("house numer"))
    street = models.TextField()
    city = models.TextField()
    county = models.TextField()
    postcode = models.TextField()
