from django.db import models

class Colegio(models.Model):
   Nombre = models.CharField(max_length=40)
   Edad = models.IntegerField()
   Grado = models.CharField(max_length=15)
   Procedencia = models.CharField(max_length=40)
