from django.contrib import admin
from sensor_monitoring.models.department import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]

    list_display_links = ["name"]

    fields = ["id", "name", "description"]

    readonly_fields = ["id"]