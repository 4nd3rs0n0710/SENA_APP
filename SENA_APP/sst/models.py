from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class CentroFormacion(models.Model):
    nombre = models.CharField(max_length=200)
    regional = models.CharField(max_length=100)
    codigo_centro = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.regional}"
    
class ProgramaFormacion(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_programa = models.CharField(max_length=50, unique=True)
    centro = models.ForeignKey(CentroFormacion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
        
class Aprendiz(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=50, choices=[
        ('CC', 'CEDULA DE CUIDADANIA'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Certificado de Extranjeria'),
    ])
    numero_documento = models.CharField(max_length=20, unique=True)
    programa_formacion = models.ForeignKey(ProgramaFormacion, on_delete=models.CASCADE)
    ficha = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.ficha}"
    
    
class Instructor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=50, choices=[
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
    ])
    numero_documento = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=200)
    
    def __str__(self):
        return self.usuario.get_full_name()
    
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
    archivo = models.FileFieldl(upload_to='documentos_sst/')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(blank=True)
    programa_formacion = models.ForeignKey(ProgramaFormacion, on_delete=models.CASCADE, null=True, blank=True)
    es_general = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class InspeccionesSST(models.Model):
    area = models.CharField(max_length=200)
    fecha = models.DteTimeField(default=timezone.now)
    inspector = models.ForeingKey(User, on_delete=models.CASCADE)
    programa_formacion = models.ForeignKey(ProgramaFormacion, on_delete=models.CASCADE)
    epp_correcto = models.BooleanField(default=False)
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
    programa_formacion = models.ForeignKey(ProgramaFormacion, on_delete=models.CASCADE)
    medidaas_tomadas = models.TextField(blank=True)
    aprendiz_involucrado = models.ForeignKey(Aprendiz, on_delete=models.SET_NULL, null=True, blank=True)
    
    def _str__(self):
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