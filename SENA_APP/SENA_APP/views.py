
from django.shortcuts import render

def index(request):
    """
    Vista para renderizar la página de inicio (index.html).
    """
    return render(request, 'index.html')