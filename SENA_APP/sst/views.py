from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from sst.forms import DocumentoSSTForm, IncidenteSSTForm, InspeccionSSTForm
from sst.models import DocumentoSST, IncidenteSST, InspeccionesSST
from aprendices.models import Aprendiz
from programas.models import Programa
from instructores.models import Instructor
from django.contrib.auth.decorators import user_passes_test

@login_required
def dashboard(request):
    #Estadisticas generales
    total_documentos = DocumentoSST.objects.count()
    total_incidentes = IncidenteSST.objects.count()
    
    # Inspecciones de los ultimos 7 dias
    inspecciones_recientes = InspeccionesSST.objects.filter(
        fecha__gte=timezone.now() - timezone.timedelta(days=7)
    ).count()
    # Incidentes por nivel de riesgo
    incidentes_por_riesgo = IncidenteSST.objects.values('nivel_riesgo').annotate(total=Count('id'))
    
    # Obtener programa de formacion del usuario si es aprendiz
    programa_usuario = None
    if hasattr(request.user, 'aprendiz'):
        programa_usuario = request.user.Aprendiz.programa
        
    context = {
        'total_documentos': total_documentos,
        'total_incidentes': total_incidentes,
        'inspecciones_recientes': inspecciones_recientes,
        'incidentes_por_riesgo': incidentes_por_riesgo,
        'programa_usuario': programa_usuario,
    }
        
    return render(request, 'sst_sena/dashboard.html', context)
    

@login_required
def documentos(request):
    documentos_list = DocumentoSST.objects.all().order_by('-fecha_actualizacion')
    # Si es aprendiz, filtrar documentos de su programa o generales
    if hasattr(request.user, 'aprendiz'):
        programa = request.user.aprendiz.programa
        documentos_list = documentos_list.filter(
            Q(es_general=True) | Q(programa=programa)
        )
    if request.method == 'POST':
        form = DocumentoSSTForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sst:documentos')
    else:
        form = DocumentoSSTForm()
        context = {
            'documentos': documentos_list,
            'form': form,
        }
        return render(request, 'sst_sena/documentos.html', context)



# === Vista de Inspecciones ===
@login_required
def inspecciones(request):
    if request.method == 'POST':
        form = InspeccionSSTForm(request.POST)
        if form.is_valid():
            inspeccion = form.save(commit=False)
            inspeccion.inspector = request.user 
            inspeccion.save()
            return redirect('sst:inspecciones')
    else:
        form = InspeccionSSTForm()
            
    inspecciones_list = InspeccionesSST.objects.all().order_by('-fecha')
    
    # Estadísticas
    inspecciones_7_dias = InspeccionesSST.objects.filter(
        fecha__gte=timezone.now() - timedelta(days=7)
    ).count()
    
    hallazgos_criticos = 0  # TODO: Implementar lógica real
    
    # 2. Corrección del filtro:
    #    Se usa 'programa' en lugar de 'programa_formacion'
    #    porque ese es el nombre del campo en el modelo InspeccionesSST
    if hasattr(request.user, 'aprendiz'):
        programa = request.user.aprendiz.programa
        inspecciones_list = inspecciones_list.filter(programa=programa)
            
    context = {
        'form': form,
        'inspecciones': inspecciones_list,
        'inspecciones_7_dias': inspecciones_7_dias,
        'hallazgos_criticos': hallazgos_criticos,
    }
    return render(request, 'sst_sena/inspecciones.html', context)


# === Vista de Incidentes ===
@login_required
def incidentes(request):
    if request.method == 'POST':
        form = IncidenteSSTForm(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.reportado_por = request.user
            incidente.save()
            return redirect('sst:incidentes')
    else:
        form = IncidenteSSTForm()
            
    incidentes_list = IncidenteSST.objects.all().order_by('-fecha')
    
    # Estadísticas
    incidentes_30_dias = IncidenteSST.objects.filter(
        fecha__gte=timezone.now() - timedelta(days=30)
    ).count()
    
    incidentes_altos = IncidenteSST.objects.filter(
        Q(nivel_riesgo='ALTO') | Q(nivel_riesgo='CRITICO')
    ).count()
    
    # Calcular días sin accidentes
    ultimo_accidente = IncidenteSST.objects.filter(
        tipo='ACC'
    ).order_by('-fecha').first()
    
    if ultimo_accidente:
        dias_sin_accidentes = (timezone.now().date() - ultimo_accidente.fecha.date()).days
    else:
        dias_sin_accidentes = 365  # Valor por defecto si no hay
    
    # Filtrar por programa si es aprendiz
    if hasattr(request.user, 'aprendiz'):
        programa = request.user.aprendiz.programa
        incidentes_list = incidentes_list.filter(programa=programa)
        # Limitar el campo aprendiz_involucrado
        form.fields['aprendiz_involucrado'].queryset = Aprendiz.objects.filter(programa=programa)
            
    context = {
        'form': form,
        'incidentes': incidentes_list,
        'total_incidentes': incidentes_list.count(),
        'incidentes_30_dias': incidentes_30_dias,
        'incidentes_altos': incidentes_altos,
        'dias_sin_accidentes': dias_sin_accidentes,
    }
    return render(request, 'sst_sena/incidentes.html', context)

@login_required
@user_passes_test(Instructor)
def reportes_estadisticas(request):
    #Estadisticas para instructores
    incidentes_por_programa = IncidenteSST.objects.values(
        'programa_formacion_nombre'
    ).annotate(total=Count('id'))
    
    inspecciones_por_mes = InspeccionesSST.objects.filter(
        fecha__year=timezone.now().year
    ).extra(
        {'mes': "EXTRACT(month FROM fecha)"}
    ).values('mes').annotate(total=Count('id'))
    
    context = {
        'incidentes_por_programa': incidentes_por_programa,
        'inspecciones_por_mes': inspecciones_por_mes,
    }
    return render(request, 'sst/reportes.html', context)

def ver_inspeccion(request, pk):
    # Obtiene el objeto de inspección especifico o devuelve un error 404 si no existe
    inspeccion = get_object_or_404(InspeccionesSST, pk=pk)
    
    context = {
        'inspeccion': inspeccion
    }
    return render(request, 'sst_sena/ver_inspeccion.html', context)