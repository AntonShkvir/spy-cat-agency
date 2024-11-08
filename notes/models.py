from django.db import models
from targets.models import Target


class Note(models.Model):
    text = models.TextField()
    target = models.ForeignKey(Target, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Note for {self.target.name} - {self.text}"
