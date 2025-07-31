from django.contrib import admin
from .models import Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = [
        'documento_identidad',
        'nombre', 
        'apellido',
        'telefono',
        'correo',
        'ciudad',
        'nivel_educativo'  # ajusta según tus campos
    ]
    
    list_filter = ['ciudad', 'nivel_educativo']
    search_fields = ['documento_identidad', 'nombre', 'apellido', 'correo']
    list_per_page = 20
    ordering = ['apellido', 'nombre']