from rest_framework.routers import DefaultRouter
from sensor_monitoring.apis import SensorReadViewset


router = DefaultRouter()
router.register(
    r"sensor-reads",
    SensorReadViewset,
    basename="sensor-reads",
)

urlpatterns = []
urlpatterns += router.urls