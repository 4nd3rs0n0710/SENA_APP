from django.contrib import admin
from .models import Programa

@admin.register(Programa)
class ProgramaFormacionAdmin(admin.ModelAdmin):
    list_display = [
        'codigo',
        'nombre',
        'nivel_formacion',
        'modalidad',
        'duracion_meses',
        'duracion_horas',
        'centro_formacion',
        'regional',
        'estado',
        'fecha_creacion'
    ]
    
    list_filter = ['modalidad', 'nivel_formacion', 'estado', 'regional']
    
    search_fields = [
        'codigo',
        'nombre',
        'centro_formacion',
        'regional',
        'descripcion'
    ]
    
    list_per_page = 25
    
    ordering = ['nombre', 'codigo']