from django.contrib import admin
from .models import CentroFormacion, ProgramaFormacion, Aprendiz, Instructor, DocumentoSST, InspeccionSST, IncidenteSST

@admin.register(CentroFormacion)
class CentroFormacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'regional', 'codigo_centro']
    list_filter = ['regional']
    search_fields = ['nombre', 'codigo_centro']
    
@admin.register(ProgramaFormacion)
class ProgramaFormacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo_programa', 'centro']
    list_filter = ['centro']
    search_fields = ['nombre', 'codigo_programa']
    
@admin.register(Aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tipo_documento', 'numero_documento', 'programa_formacion', 'ficha']
    list_filter = ['programa_formacion', 'tipo_documento']
    search_fields = ['usuario_first_name', 'usuario_last_name', 'numero_documento', 'ficha']
    
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tipo_documento', 'numero_documento', 'especialidad']
    list_filter = ['especialidad']
    search_fields = ['usuario_first_name', 'usuario_last_name', 'numero_documento']
    
@admin.register(InspeccionSST)
class InspeccionSSTAdmin(admin.ModelAdmin):
    list_display = ['area', 'fecha', 'inspector', 'programa_formacion']
    list_filter = ['fecha', 'programa_formacion']
    search_fields = ['area', 'observaciones']
    
@admin.register(IncidenteSST)
class IncidenteSSTAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'tipo', 'nivel_riesgo', 'reportado_por', 'programa_formacion']
    list_filter = ['tipo', 'nivel_riesgo', 'fecha']
    search_fields = ['descripcion', 'medidas_tomadas']