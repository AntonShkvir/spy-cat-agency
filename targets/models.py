from django.db import models
from missions.models import Mission

class Target(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mission', 'name')

    def __str__(self):
        return self.name