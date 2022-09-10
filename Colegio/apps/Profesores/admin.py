from django.contrib import admin
from .models import Profesores


@admin.register(Profesores)
class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'procedencia')
