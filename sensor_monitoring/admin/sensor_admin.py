from django.contrib import admin
from sensor_monitoring.models.sensor import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "sensor_type",
        "unity",
        "department",
    ]

    list_display_links = ["name"]

    fields = [
        "id",
        "name",
        "sensor_type",
        "unity",
        "department",
        "installation_date",
        "created_at",
        "updated_at",
        "is_active",
    ]

    readonly_fields = [
        "id",
        "created_at",
        "updated_at",    
    ]

    list_filter = [
        "department",
        "sensor_type",
    ]