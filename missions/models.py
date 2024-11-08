from django.db import models
from cats.models import SpyCat


class Mission(models.Model):
    name = models.CharField(max_length=255)
    assigned_cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
