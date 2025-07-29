from django.shortcuts import render, get_object_or_404, redirect
from .models import Aprendiz

def index(request):
    return render(request, 'index.html')

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all()
    return render(request, 'lista_aprendices.html', {'lista_aprendices': lista_aprendices})

def editar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

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
        return redirect('aprendices')  

    return render(request, 'editar_aprendiz.html', {'aprendiz': aprendiz})

def eliminar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)
    aprendiz.delete()
    return redirect('aprendices')  