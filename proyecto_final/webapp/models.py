from django.db import models
from django.utils.timezone import now


class Sacramento(models.Model):

    class Meta:
        # No database table creation or deletion operations will be performed for this model.
        abstract = True
        ordering = ["-fecha_sacramento"]

    fecha_sacramento = models.DateField(
        default=now,
        help_text="Fecha cuando se ejerció el sacramento.",
    )
    presbitero = models.CharField(
        max_length=100,
        help_text="Nombre completo del presbítero a cargo.",
    )
    libro = models.PositiveSmallIntegerField(
        help_text="Representa el número del libro según el sacramento."
    )
    pagina = models.PositiveSmallIntegerField(
        help_text="Representa el número de página según el libro."
    )
    partida = models.PositiveSmallIntegerField(
        help_text="Representa el número de partida según la página."
    )
    notas = models.CharField(
        max_length=1000,
        blank=True,
        default="N/A",
        help_text="Cualquier consideración o notas adicionales.",
    )

    def sacramento_str(self):
        return f"Oficiado el {self.fecha_sacramento} por PBRO. {self.presbitero} ({self.libro}-{self.pagina}/{self.partida})"

    def __str__(self):
        return self.sacramento_str()
