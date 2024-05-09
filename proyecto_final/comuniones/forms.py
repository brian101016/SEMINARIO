from django import forms


from .models import Comunion
from webapp.utils import (
    FechaAnteriorField,
    SexoField,
    SexoBuscarField,
    ReadOnlyFormMixin,
    BuscarSacramentoForm,
    SacramentoForm,
)


class BuscarComunionForm(BuscarSacramentoForm):
    nombre = forms.CharField(required=False)
    sexo = SexoBuscarField()
    padre = forms.CharField(required=False)
    madre = forms.CharField(required=False)
    padrino_madrina = forms.CharField(required=False)
    ciudad_bautizo = forms.CharField(required=False)
    parroquia_bautizo = forms.CharField(required=False)
    fecha_bautizo = FechaAnteriorField(required=False)


class ComunionForm(SacramentoForm):
    sexo = SexoField()
    fecha_bautizo = FechaAnteriorField(
        label="Fecha de bautizo", help_text="Fecha de cuando se recibió el bautismo."
    )

    class Meta(SacramentoForm.Meta):
        model = Comunion
        fields = "__all__"
        labels = {
            "nombre": "Nombre completo",
            "padre": "Nombre completo del padre",
            "madre": "Nombre completo de la madre",
            "padrino_madrina": "Nombre completo del padrino o madrina",
            "ciudad_bautizo": "Ciudad y lugar de bautizo",
            "parroquia_bautizo": "Parroquia de bautizo",
        }


class EliminarComunionForm(ReadOnlyFormMixin, ComunionForm):
    pass
