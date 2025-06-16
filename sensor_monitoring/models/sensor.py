from django.db import models
from .department import Department


class Sensor(models.Model):
    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"

    name = models.CharField(
        verbose_name="Nome do sensor",
        max_length=255,
    )
    sensor_type = models.CharField(
        verbose_name="Tipo do sensor",
        max_length=255,
    )
    unity = models.CharField(
        verbose_name="Unidade de medida de referência",
        max_length=255,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        verbose_name="Setor",
    )
    installation_date = models.DateField(
        verbose_name="Data de instalação",
    )
    created_at = models.DateTimeField(
        verbose_name="Criado em",
        auto_now_add=True, # data de criação automática
    )
    updated_at = models.DateTimeField(
        verbose_name="Atualizado em",
        auto_now=True,
    )
    is_active = models.BooleanField(
        verbose_name="Ativo",
        default=True,
    )

    def __str__(self):
        return self.name