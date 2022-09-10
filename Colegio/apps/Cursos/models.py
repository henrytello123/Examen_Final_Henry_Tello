from django.db import models

class Colegio(models.Model):
   Nombre = models.CharField(max_length=40)
   Horas_por_semana = models.CharField(max_length=2)
