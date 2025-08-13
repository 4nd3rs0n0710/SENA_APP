from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy

from instructores.models import Instructor
from instructores.forms import InstructorForm


# 📌 Vista de lista de instructores
def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('apellido', 'nombre')
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))


# 📌 Vista de detalle de un instructor
def detalle_instructor(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    template = loader.get_template('detalle_instructor.html')

    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    return HttpResponse(template.render(context, request))


# 📌 Vista basada en clases para crear instructor
class InstructorFormView(FormView):
    template_name = 'crear_instructor.html'
    form_class = InstructorForm
    success_url = reverse_lazy('instructores:lista_instructores')

    def form_valid(self, form):
        instructor = form.save()
        messages.success(
            self.request,
            f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# 📌 Vista basada en función para crear instructor
def crear_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            try:
                instructor = form.save()
                messages.success(
                    request,
                    f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.'
                )
                return redirect('instructores:lista_instructores')
            except Exception as e:
                messages.error(request, f'Error al guardar el instructor: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = InstructorForm()

    return render(request, 'crear_instructor.html', {
        'form': form,
        'titulo': 'Registrar Nuevo Instructor'
    })


# 📌 Vista basada en clases para editar instructor
class InstructorUpdateView(UpdateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'  # Reutilizamos la misma plantilla
    success_url = reverse_lazy('instructores:lista_instructores')

    def form_valid(self, form):
        instructor = form.save()
        messages.success(
            self.request,
            f'El instructor {instructor.nombre} {instructor.apellido} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)
