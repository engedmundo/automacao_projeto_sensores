from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    name = models.CharField(
        verbose_name="Nome do setor",
        max_length=255,
    )
    description = models.CharField(
        verbose_name="Descrição do setor",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

