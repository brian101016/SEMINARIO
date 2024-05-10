from django import forms


from .models import Bautizo
from webapp.utils import (
    FechaAnteriorField,
    SexoField,
    SexoBuscarField,
    ReadOnlyFormMixin,
    BuscarSacramentoForm,
    SacramentoForm,
)


class BuscarBautizoForm(BuscarSacramentoForm):
    """Campos específicos para buscar 'Bautizos'."""

    nombre = forms.CharField(required=False)
    sexo = SexoBuscarField()
    fecha_nacimiento_min = FechaAnteriorField(required=False)
    fecha_nacimiento_max = FechaAnteriorField(required=False)
    ciudad_nacimiento = forms.CharField(required=False)
    folio_acta_nacimiento = forms.CharField(required=False)
    padre = forms.CharField(required=False)
    madre = forms.CharField(required=False)
    abuelos_paternos = forms.CharField(required=False)
    abuelos_maternos = forms.CharField(required=False)
    padrino = forms.CharField(required=False)
    madrina = forms.CharField(required=False)
    notas_marginales = forms.CharField(required=False)


class BautizoForm(SacramentoForm):
    """Contiene campos y validaciones para crear y modificar 'Bautizos'."""

    # Sobreescribimos los campos autogenerados para considerar otras validaciones.
    sexo = SexoField()
    fecha_nacimiento = FechaAnteriorField(
        label="Fecha de nacimiento", help_text="Fecha de nacimiento del bebé."
    )

    class Meta(SacramentoForm.Meta):
        """Metadatos del formulario, hacemos lo siguiente:

        1. Heredamos todos los metadatos anteriores (de SacramentoForm.Meta).
        2. Establecemos el modelo para guardar en la BD (Bautizo).
        3. Ordenamos los campos según su importancia.
        4. Colocamos los 'labels' que hagan falta.
        5. Agregamos los campos y labels desde 'SacramentoForm.Meta'.
        """

        model = Bautizo
        fields = [
            "nombre",
            "sexo",
            "fecha_nacimiento",
            "ciudad_nacimiento",
            "folio_acta_nacimiento",
            "padre",
            "madre",
            "abuelos_paternos",
            "abuelos_maternos",
            "padrino",
            "madrina",
            "notas_marginales",
        ] + SacramentoForm.Meta.fields
        labels = {
            "nombre": "Nombre completo del bebé",
            "ciudad_nacimiento": "Ciudad y lugar de nacimiento",
            "folio_acta_nacimiento": "Folio del acta de nacimiento según como aparezca en el registro civil",
            "padre": "Nombre completo del padre",
            "madre": "Nombre completo de la madre",
            "abuelos_paternos": "Abuelos paternos",
            "abuelos_maternos": "Abuelos maternos",
            "padrino": "Nombre completo del padrino",
            "madrina": "Nombre completo de la madrina",
            "notas_marginales": "Notas marginales aplicables",
        } | SacramentoForm.Meta.labels

    def clean(self):
        """Validación final entre 'fecha_nacimiento' >= 'fecha_sacramento'."""

        data = super().clean()  # Datos validados normalmente

        fecha_nac = data["fecha_nacimiento"]
        fecha_sac = data["fecha_sacramento"]

        # Si por alguna razón no existen, marcamos error antes de evaluar.
        if fecha_nac == None or fecha_sac == None:
            raise forms.ValidationError(
                "Por favor ingresa una fecha válida", "invalid_date"
            )

        # Revisamos si los datos son coherentes.
        if fecha_nac >= fecha_sac:
            self.add_error(
                "fecha_sacramento",
                error=forms.ValidationError(
                    "La Fecha de Sacramento no puede ser menor que la Fecha de Nacimiento",
                    "invalid_date",
                ),
            )

        return data


class EliminarBautizoForm(ReadOnlyFormMixin, BautizoForm):
    """Posee todos los campos desactivados para confirmar los datos."""

    pass
