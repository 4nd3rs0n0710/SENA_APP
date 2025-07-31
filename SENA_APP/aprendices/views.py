# SENA_App/aprendices/views.py
from django.shortcuts import render, get_object_or_404, redirect
# Asegúrate de que el modelo Aprendiz esté importado correctamente
from .models import Aprendiz

# No debe haber una función 'index' aquí, ya que se maneja en la app principal.

def lista_aprendices(request):
    """
    Vista para mostrar la lista de todos los aprendices.
    """
    # Obtener todos los aprendices ordenados por apellido y nombre
    aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')

    context = {
        'lista_aprendices': aprendices,
        'total_aprendices': aprendices.count(),
    }
    return render(request, 'lista_aprendices.html', context)


def editar_aprendiz(request, aprendiz_id):
    """
    Vista para editar la información de un aprendiz específico.
    """
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)

    if request.method == 'POST':
        aprendiz.documento_identidad = request.POST.get('documento_identidad')
        aprendiz.tipo_documento = request.POST.get('tipo_documento') # Asegúrate de que esto venga del formulario
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
        return redirect('aprendices:lista_aprendices') # Redirige a la lista después de guardar

    context = {
        'aprendiz': aprendiz
    }
    return render(request, 'editar_aprendiz.html', context) # Asegúrate de tener el template 'editar_aprendiz.html'

def eliminar_aprendiz(request, aprendiz_id):
    """
    Vista para eliminar un aprendiz.
    """
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        aprendiz.delete()
        return redirect('aprendices:lista_aprendices')
    # Si no es POST, puedes mostrar una página de confirmación de eliminación
    return render(request, 'confirmar_eliminar_aprendiz.html', {'aprendiz': aprendiz}) # Asegúrate de tener el template 'confirmar_eliminar_aprendiz.html'