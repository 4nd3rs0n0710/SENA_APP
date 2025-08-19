from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Programa
from .forms import ProgramaForm 

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programas.html')
    
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    
    return HttpResponse(template.render(context, request))

def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programas:lista_programas')
    else:
        form = ProgramaForm()
    return render(request, 'crear_programas.html', {'form': form})

def editar_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('programas:detalle_programa', programa_id=programa.id)
    else:
        form = ProgramaForm(instance=programa)
    
    return render(request, 'editar_programa.html', {'form': form, 'programa': programa})
