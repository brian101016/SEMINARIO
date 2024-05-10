from django.forms import (
    DateField,
    DateInput,
    BooleanField,
    RadioSelect,
    NullBooleanField,
    Select,
    ModelForm,
    Form,
    IntegerField,
    CharField,
    Textarea,
)
from django.core.exceptions import ValidationError
import datetime


class ReadOnlyFormMixin(ModelForm):
    """Mixin que convierte a un Form como 'Read Only'.

    Se marcan todos los campos del formulario como deshabilitados y
    además se deshabilita el método 'save()'.
    """

    def __init__(self, *args, **kwargs):
        # Preservamos los campos del super().
        super(ReadOnlyFormMixin, self).__init__(*args, **kwargs)

        # Marcamos todos los campos como disabled.
        for key in self.fields.keys():
            self.fields[key].widget.attrs["readonly"] = True
            self.fields[key].disabled = True

    def save(self, *args, **kwargs):
        pass  # Sobreescribir para no hacer nada.


class FechaAnteriorField(DateField):
    """Similar a 'DateField' pero con validación de fechas anteriores.

    Además, se incluye un widget de calendario mediante un HTML Input.
    """

    def __init__(self, *args, **kwargs):
        # Valores iniciales por defecto.
        required = kwargs.pop("required", True)
        input_formats = kwargs.pop("input_formats", ["%Y-%m-%d"])
        widget = DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date", "max": datetime.date.today().isoformat()},
        )

        # Vinculamos el super() con esta clase.
        super(DateField, self).__init__(
            *args,
            **kwargs,
            required=required,
            input_formats=input_formats,
            widget=widget,
        )

    def clean(self, value):
        """Validación de fechas pasadas válidas."""

        fecha = super().clean(value=value)  # Validamos normalmente.

        if fecha == None:
            return fecha

        # Utilizamos el módulo 'datetime'.
        if fecha > datetime.date.today() + datetime.timedelta(days=1):
            raise ValidationError(
                "Por favor ingrese una fecha igual o anterior a hoy", "future_date"
            )

        return fecha  # Ahora es fecha válida.


class SexoField(BooleanField):
    """Similar a 'BooleanField' pero mediante Radio Buttons."""

    def __init__(self, *args, **kwargs):
        # Valores iniciales por defecto.
        required = kwargs.pop("required", True)
        widget = RadioSelect(choices=SEXO_CHOICE)

        # Vinculamos el super() con esta clase.
        super(BooleanField, self).__init__(
            *args, **kwargs, required=required, widget=widget
        )

    error_messages = {
        "required": "Ingrese 'Hombre' o 'Mujer'",
    }

    def validate(self, value):
        """Sobreescribe la validación default de 'BooleanField'."""

        if value != False and value != True and self.required:
            raise ValidationError(self.error_messages["required"], code="required")


class SexoBuscarField(NullBooleanField):
    """Similar a 'SexoField' pero aceptando cualquier valor."""

    def __init__(self, *args, **kwargs):
        # Valores iniciales por defecto.
        required = kwargs.pop("required", False)
        widget = Select(choices=SEXO_CHOICE_ANY)

        # Vinculamos el super() con esta clase.
        super(BooleanField, self).__init__(
            *args, **kwargs, required=required, widget=widget
        )

    error_messages = {
        "invalid": "Ingrese 'Hombre', 'Mujer' o 'Cualquiera'",
    }


class SacramentoForm(ModelForm):
    """Modelo base para los sacramentos.

    Funciona como shortcut para incluir los datos básicos en cada
    formulario de cada sacramento.
    """

    # Sobreescribimos los campos autogenerados para considerar otras validaciones.
    fecha_sacramento = FechaAnteriorField(
        label="Fecha de este sacramento",
        help_text="Fecha cuando se ejerció el sacramento.",
    )

    class Meta:
        """Metadatos del formulario, hacemos lo siguiente:

        1. Seleccionamos todos los campos básicos.
        2. Colocamos labels básicos por defecto.
        3. Convertimos las notas adicionales en un 'Textarea'.
        """

        fields = [
            "fecha_sacramento",
            "presbitero",
            "libro",
            "pagina",
            "partida",
            "notas",
        ]
        labels = {
            "presbitero": "Presbítero a cargo",
            "libro": "Número del libro",
            "pagina": "Número de la página",
            "partida": "Número de la partida",
            "notas": "Notas adicionales (opcional)",
        }

        widgets = {
            "notas": Textarea(attrs={"cols": 50, "rows": 4}),
        }


class BuscarSacramentoForm(Form):
    """Modelo base para buscar sacramentos.

    Funciona como shortcut para incluir los datos básicos en cada
    formulario de búsqueda de cada sacramento.
    """

    fecha_sacramento_min = FechaAnteriorField(required=False)
    fecha_sacramento_max = FechaAnteriorField(required=False)
    presbitero = CharField(required=False)
    libro_min = IntegerField(min_value=0, required=False)
    libro_max = IntegerField(min_value=0, required=False)
    pagina_min = IntegerField(min_value=0, required=False)
    pagina_max = IntegerField(min_value=0, required=False)
    partida_min = IntegerField(min_value=0, required=False)
    partida_max = IntegerField(min_value=0, required=False)
    notas = CharField(required=False)


# Opciones a seleccionar para 'SexoField' y 'SexoBuscarField'.
SEXO_CHOICE = [(False, "Hombre"), (True, "Mujer")]
SEXO_CHOICE_ANY = [(None, "Cualquiera"), (False, "Hombre"), (True, "Mujer")]
