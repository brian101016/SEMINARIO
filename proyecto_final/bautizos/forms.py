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
    nombre = forms.CharField(max_length=255, required=False)
    sexo = SexoBuscarField()
    fecha_nacimiento = FechaAnteriorField(required=False)
    ciudad_nacimiento = forms.CharField(max_length=255, required=False)
    folio_acta_nacimiento = forms.CharField(max_length=255, required=False)
    padre = forms.CharField(max_length=255, required=False)
    madre = forms.CharField(max_length=255, required=False)
    abuelos_paternos = forms.CharField(max_length=255, required=False)
    abuelos_maternos = forms.CharField(max_length=255, required=False)
    padrino = forms.CharField(max_length=255, required=False)
    madrina = forms.CharField(max_length=255, required=False)
    notas_marginales = forms.CharField(max_length=255, required=False)


class BautizoForm(SacramentoForm):
    sexo = SexoField()
    fecha_nacimiento = FechaAnteriorField(
        label="Fecha de nacimiento", help_text="Fecha de nacimiento del bebé."
    )

    class Meta(SacramentoForm.Meta):
        model = Bautizo
        fields = "__all__"
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


class EliminarBautizoForm(ReadOnlyFormMixin, BautizoForm):
    pass
