from django.contrib import admin
from sensor_monitoring.models.sensor_read import SensorRead


@admin.register(SensorRead)
class SensorReadAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sensor",
        "value",
        "read_time",
    ]

    list_display_links = ["sensor"]

    fields = [
        "id",
        "sensor",
        "value",
        "read_time",
    ]

    readonly_fields = ["id"]

    list_filter = [
        "sensor",
        "read_time",
    ]