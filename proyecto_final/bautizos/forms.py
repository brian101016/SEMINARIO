from django.forms import ModelForm

from Bautizo.models import Bautizos

class BautizosForm(ModelForm):
    class Meta:
        model = Bautizos
        fields = ['nombre',
        'sexo',
        'fecha_nacimiento',
        'ciudad_sacramento',
        'folio_acta_nacimiento',
        'padre',
        'madre',
        'abuelos_paternos',
        'abuelos_maternos',
        'padrino',
        'madrina',
        'notas_marginales',
        'fecha_sacramento',
        'presbitero',
        'libro',
        'pagina',
        'partida',
        'notas']