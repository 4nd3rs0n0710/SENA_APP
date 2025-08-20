from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Programa
from .forms import ProgramaForm 

def programas(request):
    """
    Muestra la lista de todos los programas registrados y el total.
    """
    lista_programas = Programa.objects.all().order_by('nombre')
    total_programas = lista_programas.count()
    context = {
        'lista_programas': lista_programas,
        'total_programas': total_programas,
    }
    return render(request, 'lista_programas.html', context)

def detalle_programa(request, programa_id):
    """
    Muestra los detalles de un programa específico, incluyendo los cursos asociados.
    """
    programa = get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    
    return render(request, 'detalle_programas.html', context)

def crear_programa(request):
    """
    Permite a los usuarios crear un nuevo programa.
    """
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programas:programas')
    else:
        form = ProgramaForm()
        
    return render(request, 'crear_programas.html', {'form': form})

def editar_programa(request, programa_id):
    """
    Permite a los usuarios editar un programa existente.
    """
    programa = get_object_or_404(Programa, id=programa_id)
    
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('programas:detalle_programa', programa_id=programa.id)
    else:
        form = ProgramaForm(instance=programa)
    
    return render(request, 'editar_programa.html', {'form': form, 'programa': programa})