from rest_framework import serializers
from .models import Note
from targets.models import Target

class NoteSerializer(serializers.ModelSerializer):
    target = serializers.PrimaryKeyRelatedField(queryset=Target.objects.all(), required=True)


    class Meta:
        model = Note
        fields = ['id', 'text', 'target']

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if instance.target.is_completed or instance.target.mission.is_completed:
            raise serializers.ValidationError("Notes cannot be updated as the target or mission is already completed.")

        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    def destroy(self, instance, validated_data):
        if instance.target.is_completed or instance.target.mission.is_completed:
            raise serializers.ValidationError("Notes cannot be updated as the target or mission is already completed.")

        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

