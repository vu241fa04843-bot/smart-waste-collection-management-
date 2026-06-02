from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Citizen', 'Citizen'),
        ('Driver', 'Driver'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Citizen'
    )

    def __str__(self):
        return self.username