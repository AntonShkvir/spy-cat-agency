from rest_framework import serializers

from notes.serializers import NoteSerializer
from .models import Target


class TargetSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'is_completed', 'notes']

    def mark_as_completed(self, target):
        target.is_completed = True
        target.save()
        if not target.mission.targets.filter(is_completed=False).exists():
            target.mission.is_completed = True
            target.mission.save()
