from django.db import models
from .sensor import Sensor


class SensorRead(models.Model):
    class Meta:
        verbose_name = "Leitura do Sensor"
        verbose_name_plural = "Leituras dos Sensores"

    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        verbose_name="Sensor",
    )
    value = models.FloatField(
        verbose_name="Valor da leitura",
    )
    read_time = models.DateTimeField(
        verbose_name="Tempo da leitura"
    )

    def __str__(self):
        return f"{self.sensor.name} - {self.read_time.strftime('%d/%m/%Y-%H:%M:%S')}"
