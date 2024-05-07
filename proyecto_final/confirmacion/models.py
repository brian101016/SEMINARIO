from django.db import models

class Confirmacion(models.Model):
    nombre = models.CharField(max_length=200,blank=False,help_text="Nombre completo de quien recibe el sacramento.")
    sexo = models.BooleanField(default=False,help_text="Sexo según: 'False' para hombre, 'True' para mujer.")
    padre = models.CharField(max_length=200,blank=False,help_text="Nombre completo del padre.")
    madre = models.CharField(max_length=200,blank=False,help_text=" Nombre completo de la madre.")
    padrino_madrina = models.CharField(max_length=200,blank=False,help_text="Nombre completo del padrino o madrina.")
    parroquia_bautizo = models.CharField(max_length=100,blank=False,help_text="Parroquia donde se recibió el bautismo.")
    ciudad_bautizo = models.CharField(max_length=50,blank=False,help_text="Ciudad donde se recibió el bautismo.")
    fecha_bautizo = models.DateField(auto_now=True,help_text="Fecha de cuando se recibió el bautismo.")

class Meta:
    ordering = ["-fecha_bautizo"]