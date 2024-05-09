from django.db import models


from webapp.models import Sacramento


class Comunion(Sacramento):

    class Meta:
        ordering = ["-fecha_sacramento", "nombre"]

    nombre = models.CharField(
        max_length=100,
        help_text="Nombre completo de quien recibe el sacramento.",
    )
    sexo = models.BooleanField(
        help_text="Sexo según: 'False' para hombre, 'True' para mujer."
    )
    padre = models.CharField(
        max_length=100,
        help_text="Nombre completo del padre."
    )
    madre = models.CharField(
        max_length=100,
        help_text="Nombre completo de la madre."
    )
    padrino_madrina = models.CharField(
        max_length=100,
        help_text="Nombre completo del padrino o madrina."
    )
    ciudad_bautizo = models.CharField(
        max_length=100,
        default="Hermosillo, Sonora",
        help_text="Parroquia donde se recibió el bautismo.",
    )
    parroquia_bautizo = models.CharField(
        max_length=100,
        help_text="Ciudad donde se recibió el bautismo."
    )
    fecha_bautizo = models.DateField(
        help_text="Fecha de cuando se recibió el bautismo."
    )

    def __str__(self):
        text = self.sacramento_str()
        return f"Comunión de {self.nombre}. " + text
