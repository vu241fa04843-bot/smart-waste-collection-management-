from django.db import models

class WasteBin(models.Model):

    bin_name = models.CharField(max_length=100)

    latitude = models.FloatField()

    longitude = models.FloatField()

    fill_level = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        default='Empty'
    )

    def __str__(self):
        return self.bin_name