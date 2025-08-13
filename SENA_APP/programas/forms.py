from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    """
    Formulario basado en el modelo Programa para crear y editar instancias.
    """
    class Meta:
        # Vinculamos el formulario al modelo Programa
        model = Programa
        # Especificamos los campos que queremos incluir en el formulario
        # Excluimos 'fecha_registro' porque se genera automáticamente
        fields = [
            'codigo', 'nombre', 'nivel_formacion', 'modalidad', 
            'duracion_meses', 'duracion_horas', 'descripcion', 
            'competencias', 'perfil_egreso', 'requisitos_ingreso', 
            'centro_formacion', 'regional', 'estado', 'fecha_creacion'
        ]
        # Podemos personalizar los widgets para un mejor control del HTML
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'perfil_egreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control'}),
            'regional': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            # Usamos un widget específico para la fecha
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        # También puedes personalizar las etiquetas si lo deseas
        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre del Programa',
            'nivel_formacion': 'Nivel de Formación',
            'modalidad': 'Modalidad',
            'duracion_meses': 'Duración (en meses)',
            'duracion_horas': 'Duración (en horas)',
            'descripcion': 'Descripción del Programa',
            'competencias': 'Competencias a Desarrollar',
            'perfil_egreso': 'Perfil de Egreso',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'regional': 'Regional',
            'estado': 'Estado',
            'fecha_creacion': 'Fecha de Creación',
        }
