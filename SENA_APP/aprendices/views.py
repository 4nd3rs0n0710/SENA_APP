from django.shortcuts import render, get_object_or_404, redirect
from .models import Aprendiz


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