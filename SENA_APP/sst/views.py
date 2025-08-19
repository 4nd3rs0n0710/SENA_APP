from datetime import timezone
from django.shortcuts import redirect, render

# En la vista de inspecciones
@login_required
def inspecciones(request):
    if request.method == 'POST':
        form = InspeccionSSTForm(request.POST)
        if form.is_valid():
            inspeccion = form.save(commit=False)
            inspeccion.inspector = request.user 
            inspeccion.save()
            return redirect('sst_sena:inspecciones')
        else:
            form = InspeccionSSTForm()
            
        inspecciones_list = InspeccionSST.objects.all().order_by('-fecha')
        
        # Variables para estadísticas
        inspecciones_7_dias = InspeccionSST.objects.filter(
            fecha_gte=timezone.now() - timezone.timedelta(days=7)
        ).count()
        
        hallazgos_criticos = 0 # Aqui se implementara la lógica para hallazgos críticos
        
        # Sí es aprendiz, filtrar inspecciones de su programa
        if hasattr(request.user, 'aprendiz'):
            programa = request.user.aprendiz.programa_formacion
            inspecciones_list = inspecciones_list.filter(programa_formacion=programa)
            
        context = {
            'form': form,
            'inspecciones': inspecciones_list,
            'inspecciones_7_dias': inspecciones_7_dias,
            'hallazgos_criticos': hallazgos_criticos,
        }
        return render(request, 'sst_sena/inspecciones.html', context)
    
    # En la vista de incidentes
    @login_required
    def incidentes(request):
        if request.method == 'POST':
            form = IncidenteSSTForm(request.POST)
            if form.is_valid():
                incidente = form.save(commit=False)
                incidente.reportado_por = request.user
                incidente.save()
                return redirect('sst_sena:incidentes')
        else:
            form = IncidenteSSTForm()
            
        incidentes_list = IncidenteSST.objects.all().order_by('-fecha')
        
        # Variables para estadisticas
        incidentes_30_dias = IncidenteSST.objects.filter(
            fecha__gte=timezone.now() - timezone.timedelta(days=30)
        ).count()
        
        incidentes_altos = IncidenteSST.objects.filter(
            Q(nivel_riesgo='ALTO') | Q(nivel_riesgo='CRITICO')
        ).count()
        
        # Calcular días sin accidentes (ejemplo simplificado)
        ultimo_accidente = IncidenteSST.objects.filter(
            tipo='ACC'
        ).order_by('-fecha').first()
        
        if ultimo_accidente:
            dias_sin_accidentes = (timezone.now().date() - ultimo_accidente.fecha.date()).days
        else:
            dias_sin_accidentes = 365 # Si no hay accidentes registrados
            
        # Si es aprendiz, filtrar incidentes de su programa
        if hasattr(request.user, 'aprendiz'):
            programa = request.user.aprendiz.programa_formacion
            incidentes_list  = incidentes_list.filter(programa_formacion=programa)
            # Limitar el campo de aprendiz_involucrado a los de su programa
            form.fields['aprenndiz_involucrado'].queryset = Aprendiz.objects.filter(programa_formacion=programa)
            
        context = {
            'form': form,
            'incidentes': incidentes_list,
            'total_incidentes': incidentes_list.count(),
            'incidentes_30_dias': incidentes_30_dias,
            'incidentes_altos': incidentes_altos,
            'dias_sin_accidentes': dias_sin_accidentes,
        }
        return render(request, 'sst_sena/incidentes.html', context)
