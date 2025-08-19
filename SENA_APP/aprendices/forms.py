from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    documento_identidad = forms.CharField(max_length=20, label="Documento de Identidad")
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    telefono = forms.CharField(max_length=10, label="Teléfono", required=False)
    correo = forms.EmailField(label="Correo Electrónico", required=False)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'type': 'date'}))
    ciudad = forms.CharField(max_length=100, required=False, label="Ciudad")

    class Meta:
        model = Aprendiz
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        
        if not documento or not nombre or not apellido:
            raise forms.ValidationError("Todos los campos son obligatorios.")
        
        return cleaned_data
    
    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números")
        return documento
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números")
        return telefono
    
    def save(self, commit=True):
        aprendiz = super().save(commit=False)
        if commit:
            aprendiz.save()
        return aprendiz
