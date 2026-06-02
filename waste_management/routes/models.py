from django.db import models
from accounts.models import User

class Route(models.Model):

    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    route_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.route_name