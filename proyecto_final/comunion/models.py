from django.db import models


class Comunion(models.Model):
    nombre = models.CharField(max_length=255)
    sexo = models.BooleanField(default=False)
    padre = models.CharField(max_length=255)
    madre = models.CharField(max_length=255)
    padrino_madrina = models.CharField(max_length=255)
    ciudad_bautizo = models.CharField(max_length=255, default="Hermosillo, Sonora")
    parroquia_bautizo = models.CharField(max_length=255)
    fecha_bautizo = models.DateField()

    def __str__(self):
        return self.nombre
