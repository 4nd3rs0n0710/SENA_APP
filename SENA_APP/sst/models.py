from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Importaciones de los modelos de las demas apps
from programas.models import Programa 
from aprendices.models import Aprendiz
from instructores.models import Instructor

# Create your models here.
class CentroFormacion(models.Model):
    nombre = models.CharField(max_length=200)
    regional = models.CharField(max_length=100)
    codigo_centro = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.regional}"

        
class DocumentoSST(models.Model):
    TIPO_DOCUMENTO = [
        ('POL', 'Politica de SST'),
        ('PRO', 'Procedimiento'),
        ('INS', 'Instructivo'),
        ('FOR', 'Formato'),
        ('PLA', 'Plan de Emergencia'),
        ('REG', 'Reglamento de Higiene y Seguridad')
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=3, choices=TIPO_DOCUMENTO)
    archivo = models.FileField(upload_to='documentos_sst/')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(blank=True)
    programa_formacion = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True)
    es_general = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class InspeccionesSST(models.Model):
    area = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    programa_formacion = models.ForeignKey(Programa, on_delete=models.CASCADE)
    epp_correcta = models.BooleanField(default=False)
    herramientas_adecuadas = models.BooleanField(default=False)
    ventilacion_verificada = models.BooleanField(default=False)
    senalizacion_visible = models.BooleanField(default=False)
    area_ordenada = models.BooleanField(default=False)
    equipos_apagados = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Inpeccion en {self.area} - {self.fecha.strftime('%Y-%m-%d')}"
    
class IncidenteSST(models.Model):
    NIVEL_RIESGO = [
        ('BAJO', 'Bajo'),
        ('MEDIO', 'Medio'),
        ('ALTO', 'Alto'),
        ('CRITICO', 'Critico'),
    ]
    
    TIPO_INCIDENTE = [
        ('ACC', 'Accidente'),
        ('INC', 'Incidente'),
        ('NOV', 'Novedad'),
        ('OBS', 'Observacion'),
    ]
    
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=3, choices=TIPO_INCIDENTE, default='OBS')
    nivel_riesgo = models.CharField(max_length=10, choices=NIVEL_RIESGO)
    reportado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    programa_formacion = models.ForeignKey(Programa, on_delete=models.CASCADE)
    medidas_tomadas = models.TextField(blank=True)
    aprendiz_involucrado = models.ForeignKey(Aprendiz, on_delete=models.SET_NULL, null=True, blank=True)
    instructor_responsable = models.ForeignKey("instructores.Instructor", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Incidente {self.id} - {self.get_nivel_riesgo_display()}"
    
    def get_risk_color_class(self):
        if self.nivel_riesgo == 'BAJO':
            return 'color-bajo'
        elif self.nivel_riesgo == 'MEDIO':
            return 'color-medio'
        elif self.nivel_riesgo == 'ALTO':
            return 'color-alto'
        elif self.nivel_riesgo == 'CRITICO':
            return 'color-critico'
        return ''