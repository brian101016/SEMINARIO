from django.db import models


from webapp.models import Sacramento


class Bautizo(Sacramento):
    """Información específica que contiene un bautizo."""

    class Meta:
        ordering = ["-fecha_sacramento", "nombre"]

    nombre = models.CharField(
        max_length=100,
        help_text="Nombre completo del bebé.",
    )
    sexo = models.BooleanField(
        help_text="Sexo según: 'False' para hombre, 'True' para mujer."
    )
    fecha_nacimiento = models.DateField(
        help_text="Fecha de nacimiento del bebé."
    )
    ciudad_nacimiento = models.CharField(
        max_length=100,
        default="Hermosillo, Sonora",
        help_text="Ciudad y lugar de nacimiento."
    )
    folio_acta_nacimiento = models.CharField(
        max_length=32,
        help_text="Folio del acta de nacimiento según como aparezca en el registro civil."
    )
    padre = models.CharField(
        max_length=100,
        help_text="Nombre completo del padre."
    )
    madre = models.CharField(
        max_length=100,
        help_text="Nombre completo de la madre."
    )
    abuelos_paternos = models.CharField(
        max_length=200,
        help_text="Nombre completo de los abuelos paternos, separado con espacios y coma donde sea necesario."
    )
    abuelos_maternos = models.CharField(
        max_length=200,
        help_text="Nombre completo de los abuelos maternos, separado con espacios y coma donde sea necesario."
    )
    padrino = models.CharField(
        max_length=100,
        help_text="Nombre completo del padrino."
    )
    madrina = models.CharField(
        max_length=100,
        help_text="Nombre completo de la madrina."
    )
    notas_marginales = models.CharField(
        max_length=1000,
        blank=True,
        default="N/A",
        help_text="Notas marginales aplicables."
    )

    def __str__(self):
        """Representación como cadena del bautizo."""

        text = self.sacramento_str()
        return f"Bautizo de {self.nombre}. " + text
