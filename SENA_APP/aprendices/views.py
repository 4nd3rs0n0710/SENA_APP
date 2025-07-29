from django.shortcuts import render, redirect, get_object_or_404
from .models import Aprendiz

# --- Vistas de la aplicación 'aprendices' ---

def index(request):
    """
    Vista para la página de inicio (Home).
    Renderiza el template 'index.html'.
    """
    return render(request, 'index.html')

def lista_aprendices(request):
    """
    Vista para mostrar la lista de todos los aprendices.
    """
    aprendices = Aprendiz.objects.all()
    context = {'lista_aprendices': aprendices}
    return render(request, 'lista_aprendices.html', context)

def editar_aprendiz(request, aprendiz_id):
    """
    Vista para editar la información de un aprendiz específico.
    """
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)

    if request.method == 'POST':
        aprendiz.documento_identidad = request.POST.get('documento_identidad')
        aprendiz.nombre = request.POST.get('nombre')
        aprendiz.apellido = request.POST.get('apellido')
        aprendiz.telefono = request.POST.get('telefono')
        aprendiz.correo = request.POST.get('correo')
        aprendiz.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        aprendiz.ciudad = request.POST.get('ciudad')
        aprendiz.programa = request.POST.get('programa')
        aprendiz.save()
        return redirect('lista_aprendices')

    context = {'aprendiz': aprendiz}
    return render(request, 'editar_aprendiz.html', context)

def eliminar_aprendiz(request, aprendiz_id): # <--- ¡Nueva función para eliminar!
    """
    Vista para eliminar un aprendiz de la base de datos.
    Solo permite eliminar mediante una petición POST para seguridad.
    """
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    if request.method == 'POST':
        aprendiz.delete() # Elimina el objeto Aprendiz de la base de datos
    return redirect('lista_aprendices') # Redirige a la lista de aprendices después de eliminar
