from django import forms


from .models import Confirmacion
from webapp.utils import (
    FechaAnteriorField,
    SexoField,
    SexoBuscarField,
    ReadOnlyFormMixin,
)


class BuscarConfirmacionForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=False)
    sexo = SexoBuscarField()
    padre = forms.CharField(max_length=255, required=False)
    madre = forms.CharField(max_length=255, required=False)
    padrino_madrina = forms.CharField(max_length=255, required=False)
    ciudad_bautizo = forms.CharField(max_length=255, required=False)
    parroquia_bautizo = forms.CharField(max_length=255, required=False)
    fecha_bautizo = FechaAnteriorField(required=False)


class ConfirmacionForm(forms.ModelForm):
    sexo = SexoField()
    fecha_bautizo = FechaAnteriorField(label="Fecha de bautizo")

    class Meta:
        model = Confirmacion
        fields = "__all__"
        labels = {
            "nombre": "Nombre completo",
            "padre": "Nombre completo del padre",
            "madre": "Nombre completo de la madre",
            "padrino_madrina": "Nombre completo del padrino o madrina",
            "ciudad_bautizo": "Ciudad y lugar de bautizo",
            "parroquia_bautizo": "Parroquia de bautizo",
        }


class EliminarConfirmacionForm(ReadOnlyFormMixin, ConfirmacionForm):
    pass
