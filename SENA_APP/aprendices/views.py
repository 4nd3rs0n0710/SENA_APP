from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Aprendiz, Curso
from instructores.models import Instructor
from programas.models import Programa
from .forms import AprendizForm 

def lista_aprendices(request):
    """Muestra la lista de todos los aprendices."""
    aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')
    context = {
        'lista_aprendices': aprendices,
        'total_aprendices': aprendices.count(),
    }
    return render(request, 'lista_aprendices.html', context)

def editar_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        # Nota: Usar ModelForm aquí es más seguro y sencillo que procesar los datos
        # manualmente como lo estabas haciendo.
        form = AprendizForm(request.POST, instance=aprendiz)
        if form.is_valid():
            form.save()
            return redirect('aprendices:lista_aprendices')
    else:
        # Crea una instancia del formulario con los datos del aprendiz existente.
        form = AprendizForm(instance=aprendiz)
    
    context = {
        'form': form,
        'aprendiz': aprendiz
    }
    return render(request, 'editar_aprendiz.html', context)

def eliminar_aprendiz(request, aprendiz_id):
    """Confirma y elimina un aprendiz."""
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        aprendiz.delete()
        return redirect('aprendices:lista_aprendices')
    return render(request, 'confirmar_eliminar_aprendiz.html', {'aprendiz': aprendiz})

def inicio(request):
    """Vista de la página de inicio con estadísticas."""
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count()
    total_cursos = Curso.objects.count()
    cursos_activos = Curso.objects.filter(estado__in=['INI', 'EJE']).count()
    context = {
        'total_aprendices': total_aprendices,
        'total_cursos': total_cursos,
        'cursos_activos': cursos_activos,
        'total_instructores': total_instructores,
        'total_programas': total_programas,
    }
    return render(request, 'index.html', context)

def lista_cursos(request):
    """Muestra la lista de todos los cursos."""
    cursos = Curso.objects.all().order_by('-fecha_inicio')
    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
        'titulo': 'Lista de Cursos'
    }
    return render(request, 'lista_cursos.html', context)

def detalle_curso(request, curso_id):
    """Muestra los detalles de un curso específico."""
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    return render(request, 'detalle_curso.html', context)

def detalle_aprendiz(request, aprendiz_id):
    """Muestra los detalles de un aprendiz específico."""
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    context = {
        'aprendiz': aprendiz,
    }
    return render(request, 'detalle_aprendiz.html', context)

def agregar_aprendiz(request):
    """
    Vista para agregar un nuevo aprendiz usando ModelForm.
    Esta es la función que estabas buscando para guardar los datos.
    """
    if request.method == 'POST':
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la lista de aprendices después de guardar
            return redirect('aprendices:lista_aprendices')
    else:
        form = AprendizForm()
    
    return render(request, 'agregar_aprendiz.html', {'form': form})

# Se ha eliminado la clase AprendizFormView para evitar conflictos.
# Si quieres usarla, deberías eliminar la función `agregar_aprendiz` y
# asegurarte de que tu `urls.py` esté configurado para la clase.
