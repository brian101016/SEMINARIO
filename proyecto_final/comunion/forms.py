from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, password_validation
from django.core.exceptions import ValidationError
import datetime


from usuarios.forms import ReadOnlyFormMixin
from .models import Comunion


class BuscarComunionForm(forms.Form):
    SEXO_SELECT = forms.Select(
        choices=[(None, "Cualquiera"), (False, "Hombre"), (True, "Mujer")]
    )

    nombre = forms.CharField(max_length=255, required=False)
    sexo = forms.NullBooleanField(widget=SEXO_SELECT, required=False)
    padre = forms.CharField(max_length=255, required=False)
    madre = forms.CharField(max_length=255, required=False)
    padrino_madrina = forms.CharField(max_length=255, required=False)
    ciudad_bautizo = forms.CharField(max_length=255, required=False)
    parroquia_bautizo = forms.CharField(max_length=255, required=False)
    fecha_bautizo = forms.DateField(
        required=False,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date", "max": datetime.date.today().isoformat()},
        ),
    )


class ComunionForm(forms.ModelForm):
    fecha_bautizo = forms.DateField(
        required=True,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date", "max": datetime.date.today().isoformat()},
        ),
        label="Fecha de bautizo",
    )

    class Meta:
        SEXO_CHOICE = [(False, "Hombre"), (True, "Mujer")]

        model = Comunion
        fields = "__all__"
        labels = {
            "nombre": "Nombre completo",
            "sexo": "Sexo",
            "padre": "Nombre completo del padre",
            "madre": "Nombre completo de la madre",
            "padrino_madrina": "Nombre completo del padrino o madrina",
            "ciudad_bautizo": "Ciudad y lugar de bautizo",
            "parroquia_bautizo": "Parroquia de bautizo",
        }
        widgets = {
            "sexo": forms.RadioSelect(choices=SEXO_CHOICE),
        }

    def clean_sexo(self):
        sexo = self.cleaned_data["sexo"]

        if sexo != True and sexo != False:
            raise ValidationError("Ingrese Hombre o Mujer", "no_binary")

        return sexo

    def clean_fecha_bautizo(self):
        fecha = self.cleaned_data["fecha_bautizo"]

        if fecha > datetime.date.today() + datetime.timedelta(days=1):
            raise ValidationError(
                "Por favor ingrese una fecha igual o anterior a hoy", "future_date"
            )

        return fecha


class EliminarComunionForm(ReadOnlyFormMixin, ComunionForm):
    pass
