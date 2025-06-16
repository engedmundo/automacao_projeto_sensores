from rest_framework import viewsets
from sensor_monitoring.models import SensorRead
from rest_framework.permissions import AllowAny
from .serializers import SensorReadSerializer


class SensorReadViewset(viewsets.ModelViewSet):
    queryset = SensorRead.objects.all()
    serializer_class = SensorReadSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post", "patch", "delete"]