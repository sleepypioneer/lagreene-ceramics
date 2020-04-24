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
    link = models.URLField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(default=start_date)

    def year(self):
        return self.end_date.strftime('%Y')
