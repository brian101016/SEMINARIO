from django.db import models


from webapp.models import Sacramento


class Matrimonio(Sacramento):

    class Meta:
        ordering = ["-fecha_sacramento", "novio", "novia"]

    novio = models.CharField(
        max_length=100,
        help_text="Nombre completo del novio."
    )
    novia = models.CharField(
        max_length=100,
        help_text="Nombre completo de la novia."
    )
    domicilio = models.CharField(
        max_length=100,
        help_text="Domicilio de los novios, anotado en cualquier formato."
    )
    ciudad_sacramento = models.CharField(
        max_length=100,
        default="Hermosillo, Sonora",
        help_text="Ciudad donde se recibió el sacramento en custión."
    )
    padres_novio = models.CharField(
        max_length=200,
        help_text="Nombre completo de los padres del novio, separado con espacios y una coma donde sea necesario."
    )
    padres_novia = models.CharField(
        max_length=200,
        help_text="Nombre completo de los padres de la novia, separado con espacios y una coma donde sea necesario."
    )
    testigos = models.CharField(
        max_length=500,
        help_text="Nombre completo de los testigos, separado con espacios y comas donde sea necesario."
    )
    presentacion = models.CharField(
        max_length=100,
        help_text="Presentación matrimonial o anotaciones particulares."
    )

    def __str__(self):
        text = self.sacramento_str()
        return f"Matrimonio de {self.novio} y {self.novia}. " + text
