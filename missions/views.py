from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Mission
from .serializers import MissionSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.assigned_cat is not None:
            raise ValidationError("Cannot delete a mission assigned to a cat.")
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'], url_path='mark-as-completed')
    def mark_as_completed(self, request, pk=None):
        mission = self.get_object()

        mission.is_completed = True
        mission.save()
        mission.targets.update(is_completed=True)

        return Response({"status": "Mission and all targets marked as completed."}, status=status.HTTP_200_OK)
    