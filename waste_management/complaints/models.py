from django.conf import settings
from django.db import models

class Complaint(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    location = models.CharField(max_length=200)

    description = models.TextField()

    latitude = models.FloatField(
        null=True,
        blank=True
    )

    longitude = models.FloatField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )