from rest_framework import serializers

from notes.serializers import NoteSerializer
from .models import Mission
from targets.models import Target
from cats.models import SpyCat


class TargetSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True, required=False)  # Делаем notes необязательным

    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'is_completed', 'notes']



class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)
    assigned_cat = serializers.PrimaryKeyRelatedField(queryset=SpyCat.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Mission
        fields = ['id', 'name', 'assigned_cat', 'is_completed', 'targets']
        read_only_fields = ['is_completed']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets', [])

        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)

        return mission

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.assigned_cat = validated_data.get('assigned_cat', instance.assigned_cat)
        instance.save()

        targets_data = validated_data.get('targets', [])

        instance.targets.all().delete()
        for target_data in targets_data:
            Target.objects.create(mission=instance, **target_data)

        return instance
