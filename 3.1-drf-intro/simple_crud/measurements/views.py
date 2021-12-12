from rest_framework.viewsets import ModelViewSet
from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerialiser, MeasurementSerialiser


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerialiser