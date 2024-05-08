from django.db import models

# Create your models here.
nombre = models.CharField(max_length=60)  
sexo = models.BooleanField(initial = True)
fecha_nacimiento = models.DateField()
ciudad_nacimiento = models.CharField(max_length=60) 
folio_acta_nacimiento = models.CharField(max_length=60)  
padre = models.CharField(max_length=60)  
madre = models.CharField(max_length=60)  
abuelos_paternos = models.CharField(max_length=60)
abuelos_maternos = models.CharField(max_length=60)
padrino = models.CharField(max_length=60)
madrina = models.CharField(max_length=60)
notas_marginales = models.CharField(max_length=60)  
fecha_sacramento = models.DateField()
presbitero = models.CharField(max_length=60)  
libro = models.IntegerField()
pagina = models.IntegerField()
partida = models.IntegerField()
notas = models.CharField(max_length=60)  

    #Método str para retornar algo legible
def _str_(self):
    return f"ID: {self.id}, libro{self.libro} dentro de la página {self.página}"