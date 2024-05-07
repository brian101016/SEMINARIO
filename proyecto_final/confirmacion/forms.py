from django import forms
from django.forms import ModelForm
from .models import Confirmacion

CHOICES = {
    True : "Mujer",
    False : "Hombre",
}

class ConfirmacionForm(forms.ModelForm):
    class Meta:
        model = Confirmacion
        fields = ['nombre','padre','madre','padrino_madrina','parroquia_bautizo','ciudad_bautizo']

    sexo = forms.MultipleChoiceField(
    label='Sexo: Marque la casilla',
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=CHOICES,
    )

class CrearConfirmacion(forms.Form):
    nombre = forms.CharField(label='Nombre completo', max_length=200,required=True) 
    sexo = forms.MultipleChoiceField(
        label='Sexo: Marque la casilla',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES,
    )
    padre = forms.CharField(label='Nombre completo del padre', max_length=200,required=True)
    madre = forms.CharField(label='Nombre completo de la madre', max_length=200,required=True)
    padrino_madrina = forms.CharField(label='Nombre compelto del padrino o madrina',max_length=200,required=True)
    parroquia_bautizo = forms.CharField(label='Nombre de la parroquia',max_length=100,required=True)
    ciudad_bautizo = forms.CharField(label='Nombre de la cuidad',max_length=100,required=True)