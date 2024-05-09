from django import forms


from .models import Matrimonio
from webapp.utils import (
    FechaAnteriorField,
    SexoField,
    SexoBuscarField,
    ReadOnlyFormMixin,
    BuscarSacramentoForm,
    SacramentoForm,
)


class BuscarMatrimonioForm(BuscarSacramentoForm):
    novio = forms.CharField(required=False)
    novia = forms.CharField(required=False)
    domicilio = forms.CharField(required=False)
    ciudad_sacramento = forms.CharField(required=False)
    padres_novio = forms.CharField(required=False)
    padres_novia = forms.CharField(required=False)
    testigos = forms.CharField(required=False)
    presentacion = forms.CharField(required=False)


class MatrimonioForm(SacramentoForm):
    class Meta(SacramentoForm.Meta):
        model = Matrimonio
        fields = "__all__"
        labels = {
            "novio": "Novio",
            "novia": "Novia",
            "domicilio": "Domicilio de los novios",
            "ciudad_sacramento": "Ciudad de sacramento",
            "padres_novio": "Padres del novio",
            "padres_novia": "Padres de la novia",
            "testigos": "Testigos (separados por comas)",
            "presentacion": "Presentación matrimonial",
        }


class EliminarMatrimonioForm(ReadOnlyFormMixin, MatrimonioForm):
    pass
