from django.shortcuts import render
from .models import Aprendiz
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'lista_aprendices': lista_aprendices,
    }
    return HttpResponse(template.render(context, request))