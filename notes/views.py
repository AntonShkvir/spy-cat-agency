from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.target.is_completed or instance.target.mission.is_completed:
            raise ValidationError("Notes cannot be deleted as the target or mission is already completed.")

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
