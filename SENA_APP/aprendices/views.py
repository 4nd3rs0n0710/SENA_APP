from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aprendiz, Curso
from instructores.models import Instructor
from programas.models import Programa


def lista_aprendices(request):
    aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')

    context = {
        'lista_aprendices': aprendices,
        'total_aprendices': aprendices.count(),
    }
    return render(request, 'lista_aprendices.html', context)


def editar_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)

    if request.method == 'POST':
        aprendiz.documento_identidad = request.POST.get('documento_identidad')
        aprendiz.tipo_documento = request.POST.get('tipo_documento')
        aprendiz.nombre = request.POST.get('nombre')
        aprendiz.apellido = request.POST.get('apellido')
        aprendiz.telefono = request.POST.get('telefono')
        aprendiz.correo = request.POST.get('correo')
        aprendiz.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        aprendiz.ciudad = request.POST.get('ciudad')
        aprendiz.direccion = request.POST.get('direccion')
        aprendiz.nivel_educativo = request.POST.get('nivel_educativo')
        aprendiz.programa = request.POST.get('programa')
        aprendiz.save()
        return redirect('aprendices:lista_aprendices')

    context = {
        'aprendiz': aprendiz
    }
    return render(request, 'editar_aprendiz.html', context)


def eliminar_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        aprendiz.delete()
        return redirect('aprendices:lista_aprendices')
    return render(request, 'confirmar_eliminar_aprendiz.html', {'aprendiz': aprendiz})


def inicio(request):
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count()
    total_cursos = Curso.objects.count()
    cursos_activos = Curso.objects.filter(estado__in=['INI', 'EJE']).count()  # Corregido __in
    template = loader.get_template('index.html')

    context = {
        'total_aprendices': total_aprendices,
        'total_cursos': total_cursos,
        'cursos_activos': cursos_activos,
        'total_instructores': total_instructores,
        'total_programas': total_programas,
    }

    return HttpResponse(template.render(context, request))


def lista_cursos(request):
    cursos = Curso.objects.all().order_by('-fecha_inicio')
    template = loader.get_template('lista_cursos.html')

    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
        'titulo': 'Lista de Cursos'
    }

    return HttpResponse(template.render(context, request))


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    template = loader.get_template('detalle_curso.html')

    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }

    return HttpResponse(template.render(context, request))


def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    template = loader.get_template('detalle_aprendiz.html')

    context = {
        'aprendiz': aprendiz,
    }

    return HttpResponse(template.render(context, request))
