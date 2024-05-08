from django.forms import ModelForm, EmailInput

from matrimonios.models import Matrimonio

class MatrimonioForm(ModelForm):
    class Meta:
        model = Matrimonio
        fields = ['novio',
        'novia',
        'domicilio',
        'ciudad_sacramento',
        'padres_novio',
        'padres_novia',
        'testigos',
        'presentacion',
        'fecha_sacramento',
        'presbitero',
        'libro',
        'pagina',
        'partida','notas']
       