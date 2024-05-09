from django.db import models

# Create your models here.

class Matrimonio(models.Model):

    novio = models.CharField(max_length=60)  
    novia = models.CharField(max_length=60)  
    domicilio = models.CharField(max_length=60)  
    ciudad_sacramento = models.CharField(max_length=60)  
    padres_novio = models.CharField(max_length=60)  
    padres_novia = models.CharField(max_length=60)  
    testigos = models.CharField(max_length=60) #No se pudo hacer con arreglo aquí
    presentacion = models.CharField(max_length=60)  
    fecha_sacramento = models.DateField()
    presbitero = models.CharField(max_length=60)  
    libro = models.IntegerField()
    pagina = models.IntegerField()
    partida = models.IntegerField()
    notas = models.CharField(max_length=60)  

    #Método str para retornar algo legible
    def __str__(self):
        return f"ID: {self.id}, libro{self.libro} dentro de la página {self.página}"
