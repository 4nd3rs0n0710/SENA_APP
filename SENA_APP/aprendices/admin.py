from django.contrib import admin
from .models import Aprendiz


class AprendizAdmin(admin.ModelAdmin):
    list_display = ('documento_identidad', 'nombre', 'apellido', 'telefono', 'correo', 'fecha_nacimiento', 'ciudad', 'programa')
    search_fields = ('documento_identidad', 'nombre', 'apellido', 'correo')
    list_filter = ('ciudad', 'programa')
    
admin.site.register(Aprendiz, AprendizAdmin)