from django.contrib import admin
from .models import (
    CentroFormacion,
    DocumentoSST,
    InspeccionesSST,
    IncidenteSST,
    Programa
)


@admin.register(CentroFormacion)
class CentroFormacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'regional', 'codigo_centro']
    list_filter = ['regional']
    search_fields = ['nombre', 'codigo_centro']
    ordering = ['nombre']
    list_per_page = 20

@admin.register(DocumentoSST)
class DocumentoSSTAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_subida', 'subido_por']
    list_filter = ['fecha_subida']
    search_fields = ['titulo', 'descripcion']
    ordering = ['-fecha_subida']
    list_per_page = 20

@admin.register(InspeccionesSST)
class InspeccionesSSTAdmin(admin.ModelAdmin):
    list_display = ['area', 'fecha', 'inspector', 'programa_formacion']
    list_filter = ['fecha', 'programa_formacion']
    # Cambia 'programa_formacion' a 'programa__nombre'
    search_fields = ['area', 'observaciones', 'programa__nombre'] 
    ordering = ['-fecha']
    list_per_page = 20

@admin.register(IncidenteSST)
class IncidenteSSTAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'tipo', 'nivel_riesgo', 'reportado_por', 'programa_formacion']
    list_filter = ['tipo', 'nivel_riesgo', 'fecha']
    # Cambia 'programa_formacion' a 'programa__nombre'
    search_fields = ['descripcion', 'medidas_tomadas', 'programa__nombre']
    ordering = ['-fecha']
    list_per_page = 20