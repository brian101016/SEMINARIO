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
    sexo = SexoField()
    fecha_nacimiento = FechaAnteriorField(
        label="Fecha de nacimiento", help_text="Fecha de nacimiento del bebé."
    )

    class Meta(SacramentoForm.Meta):
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
            "fecha_sacramento",
            "presbitero",
            "libro",
            "pagina",
            "partida",
            "notas",
        ]
        labels = {
            "nombre": "Nombre completo del bebé",
            "ciudad_nacimiento": "Ciudad y lugar de nacimiento",
            "folio_acta_nacimiento": "Folio del acta de nacimiento según como aparezca en el registro civil",
            "padre": "Nombre completo del padre",
            "madre": "Nombre completo de la madre",
            "abuelos_paternos": "Nombre completo de los abuelos paternos, separado con espacios y coma donde sea necesario",
            "abuelos_maternos": "Nombre completo de los abuelos maternos, separado con espacios y coma donde sea necesario",
            "padrino": "Nombre completo del padrino",
            "madrina": "Nombre completo de la madrina",
            "notas_marginales": "Notas marginales aplicables",
        }

    def clean(self):
        data = super().clean()

        fecha_nac = data["fecha_nacimiento"]
        fecha_sac = data["fecha_sacramento"]

        if fecha_nac == None or fecha_sac == None:
            raise forms.ValidationError(
                "Por favor ingresa una fecha válida", "invalid_date"
            )

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
    pass
