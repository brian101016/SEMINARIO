from django import forms


from .models import Confirmacion
from webapp.utils import (
    FechaAnteriorField,
    SexoField,
    SexoBuscarField,
    ReadOnlyFormMixin,
    BuscarSacramentoForm,
    SacramentoForm,
)


class BuscarConfirmacionForm(BuscarSacramentoForm):
    nombre = forms.CharField(required=False)
    sexo = SexoBuscarField()
    padre = forms.CharField(required=False)
    madre = forms.CharField(required=False)
    padrino_madrina = forms.CharField(required=False)
    ciudad_bautizo = forms.CharField(required=False)
    parroquia_bautizo = forms.CharField(required=False)
    fecha_bautizo_min = FechaAnteriorField(required=False)
    fecha_bautizo_max = FechaAnteriorField(required=False)


class ConfirmacionForm(SacramentoForm):
    sexo = SexoField()
    fecha_bautizo = FechaAnteriorField(
        label="Fecha de bautizo", help_text="Fecha de cuando se recibió el bautismo."
    )

    class Meta(SacramentoForm.Meta):
        model = Confirmacion
        fields = [
            "nombre",
            "sexo",
            "padre",
            "madre",
            "padrino_madrina",
            "ciudad_bautizo",
            "parroquia_bautizo",
            "fecha_bautizo",
            "fecha_sacramento",
            "presbitero",
            "libro",
            "pagina",
            "partida",
            "notas",
        ]
        labels = {
            "nombre": "Nombre completo",
            "padre": "Nombre completo del padre",
            "madre": "Nombre completo de la madre",
            "padrino_madrina": "Nombre completo del padrino o madrina",
            "ciudad_bautizo": "Ciudad y lugar de bautizo",
            "parroquia_bautizo": "Parroquia de bautizo",
        }

    def clean(self):
        data = super().clean()

        fecha_bau = data["fecha_bautizo"]
        fecha_sac = data["fecha_sacramento"]

        if fecha_bau == None or fecha_sac == None:
            raise forms.ValidationError(
                "Por favor ingresa una fecha válida", "invalid_date"
            )

        if fecha_bau >= fecha_sac:
            self.add_error(
                "fecha_sacramento",
                error=forms.ValidationError(
                    "La Fecha de Sacramento no puede ser menor que la Fecha de Bautizo",
                    "invalid_date",
                ),
            )

        return data


class EliminarConfirmacionForm(ReadOnlyFormMixin, ConfirmacionForm):
    pass
