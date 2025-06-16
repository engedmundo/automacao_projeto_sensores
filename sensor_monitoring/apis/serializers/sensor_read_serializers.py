from rest_framework import serializers
from sensor_monitoring.models import SensorRead


class SensorReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorRead
        fields = [
            "id",
            "sensor",
            "value",
            "read_time",
        ]