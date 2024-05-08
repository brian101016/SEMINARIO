from django.forms import (
    DateField,
    DateInput,
    BooleanField,
    RadioSelect,
    NullBooleanField,
    Select,
    ModelForm,
)
from django.core.exceptions import ValidationError
import datetime


class ReadOnlyFormMixin(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReadOnlyFormMixin, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs["readonly"] = True
            self.fields[key].disabled = True

    def save(self, *args, **kwargs):
        pass  # do not do anything


class FechaAnteriorField(DateField):
    def __init__(self, *args, **kwargs):

        required = kwargs.pop("required", True)
        input_formats = kwargs.pop("input_formats", ["%Y-%m-%d"])
        widget = DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date", "max": datetime.date.today().isoformat()},
        )

        super(DateField, self).__init__(
            *args,
            **kwargs,
            required=required,
            input_formats=input_formats,
            widget=widget
        )

    def clean(self, value):
        fecha = super().clean(value=value)

        if fecha == None:
            return fecha

        if fecha > datetime.date.today() + datetime.timedelta(days=1):
            raise ValidationError(
                "Por favor ingrese una fecha igual o anterior a hoy", "future_date"
            )

        return fecha


class SexoField(BooleanField):
    def __init__(self, *args, **kwargs):

        required = kwargs.pop("required", True)
        widget = RadioSelect(choices=SEXO_CHOICE)

        super(BooleanField, self).__init__(
            *args, **kwargs, required=required, widget=widget
        )

    error_messages = {
        "invalid": "Ingrese 'Hombre' o 'Mujer'",
        "invalid_nullable": "Ingrese 'Hombre' o 'Mujer'",
    }


class SexoBuscarField(NullBooleanField):
    def __init__(self, *args, **kwargs):

        required = kwargs.pop("required", False)
        widget = Select(choices=SEXO_CHOICE_ANY)

        super(BooleanField, self).__init__(
            *args, **kwargs, required=required, widget=widget
        )

    error_messages = {
        "invalid": "Ingrese 'Hombre', 'Mujer' o 'Cualquiera'",
        "invalid_nullable": "Ingrese 'Hombre', 'Mujer' o 'Cualquiera'",
    }


SEXO_CHOICE = [(False, "Hombre"), (True, "Mujer")]
SEXO_CHOICE_ANY = [(None, "Cualquiera"), (False, "Hombre"), (True, "Mujer")]
