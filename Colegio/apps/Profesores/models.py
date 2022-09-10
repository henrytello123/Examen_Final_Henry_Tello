from django.db import models

class Profesores(models.Model):
   nombre = models.CharField(max_length=40)
   procedencia = models.CharField(max_length=40)

def __str__(self):
   return "{} es un profesor procedente de {} ".format(self.nombre, self.procedencia)