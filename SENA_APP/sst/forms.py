from django import forms 
from .models import DocumentoSST, InspeccionSST, IncidenteSST, Aprendiz

class DocumentoSSTForm(forms.ModelForm):
    class Meta:
        model = DocumentoSST
        fields = ['nombre', 'tipo', 'archivo', 'descripcion', 'programa_formacion', 'es_general']
        widgets = {
            'descripcion': forms.Textsrea(attrs={'rows': 3}),
        }
        
class InspeccionSSTForm(forms.ModelForm):
    class Meta:
        model = InspeccionSST
        fields = ['area', 'programa_formacion', 'epp_correcta', 'herramientas_adecuadas', 'ventilacion_verificada', 'senalizacion_visible', 'area_ordenada', 'equipos_apagados', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 4}),
            'area': forms.TextInput(attrs={'placeholder': 'Ej: Taller de Soldadura, Laboratorio de Mineralogia...'}),
        }
        
class IncidenteSSTForm(forms.ModelForm):
    class Meta:
        model = IncidenteSST
        fields = ['descripcion', 'fecha', 'tipo', 'nivel_riesgo', 'programa_formacion', 'aprendiz_involucrado', 'medidas_tomadas']
        widgets = {
            'descripcion': forms.Textarea(attrs={'type': 'date'}),
            'medidas_tomadas': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Medidas correctivas o preventivas implementadas...'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'programa_formacion' in self.data:
            try:
                programa_id = int(self.data.get('programa_formacion'))
                self.fields['aprendiz_involucrado'].queryset = Aprendiz.objects.filter(programa_formacion_id=programa_id)
            except (ValueError, TypeError):
                pass