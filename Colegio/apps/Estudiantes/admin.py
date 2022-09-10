from django.contrib import admin
from .models import Colegio

@admin.register(Colegio)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Edad', 'Grado', 'Procedencia')
