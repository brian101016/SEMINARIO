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
    """Campos específicos para buscar 'Matrimonios'."""

    novio = forms.CharField(required=False)
    novia = forms.CharField(required=False)
    domicilio = forms.CharField(required=False)
    ciudad_sacramento = forms.CharField(required=False)
    padres_novio = forms.CharField(required=False)
    padres_novia = forms.CharField(required=False)
    testigos = forms.CharField(required=False)
    presentacion = forms.CharField(required=False)


class MatrimonioForm(SacramentoForm):
    """Contiene campos y validaciones para crear y modificar 'Matrimonios'."""

    class Meta(SacramentoForm.Meta):
        """Metadatos del formulario, hacemos lo siguiente:

        1. Heredamos todos los metadatos anteriores (de SacramentoForm.Meta).
        2. Establecemos el modelo para guardar en la BD (Matrimonio).
        3. Ordenamos los campos según su importancia.
        4. Colocamos los 'labels' que hagan falta.
        5. Agregamos los campos y labels desde 'SacramentoForm.Meta'.
        """

        model = Matrimonio
        fields = [
            "novio",
            "novia",
            "domicilio",
            "ciudad_sacramento",
            "padres_novio",
            "padres_novia",
            "testigos",
            "presentacion",
        ] + SacramentoForm.Meta.fields
        labels = {
            "novio": "Novio",
            "novia": "Novia",
            "domicilio": "Domicilio de los novios",
            "ciudad_sacramento": "Ciudad de sacramento",
            "padres_novio": "Padres del novio",
            "padres_novia": "Padres de la novia",
            "testigos": "Testigos (separados por comas)",
            "presentacion": "Presentación matrimonial",
        } | SacramentoForm.Meta.labels


class EliminarMatrimonioForm(ReadOnlyFormMixin, MatrimonioForm):
    """Posee todos los campos desactivados para confirmar los datos."""

    pass
