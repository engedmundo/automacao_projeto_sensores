from django.contrib import admin
from sensor_monitoring.models.sensor import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass