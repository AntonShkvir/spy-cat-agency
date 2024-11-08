from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def is_available(self):
        return not self.mission_set.filter(is_completed=False).exists()

    def __str__(self):
        return self.name
