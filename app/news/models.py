from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=75, blank=True)
    address_line1 = models.CharField("Address line 1", max_length=45)
    address_line2 = models.CharField("Address line 2", max_length=45, blank=True)
    postal_code = models.CharField("Postal Code", max_length=10)
    city = models.CharField(max_length=50, blank=True)


class Show(models.Model):
    title = models.CharField(max_length=75)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=200)
    when = models.DateField("when", blank=True)
    link = models.URLField(max_length=100)

    def year(self):
        return self.when.strftime('%Y')
