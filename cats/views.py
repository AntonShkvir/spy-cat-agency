from rest_framework import viewsets, status
from .models import SpyCat
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import SpyCatSerializer, SpyCatSalarySerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return SpyCatSalarySerializer
        return SpyCatSerializer
