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
    fecha_nacimiento = FechaAnteriorField(required=False)
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
