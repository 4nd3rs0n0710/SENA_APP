# programas/urls.py
from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    # URL para ver la lista de programas
    # El nombre de la vista en views.py es 'programas'
    path('', views.programas, name='lista_programas'),
    
    # URL para crear un nuevo programa
    path('crear/', views.crear_programa, name='crear_programa'),
    
    # URL para ver el detalle de un programa específico
    path('<int:programa_id>/', views.detalle_programa, name='detalle_programa'),

    # URL para editar un programa existente
    path('<int:programa_id>/editar/', views.editar_programa, name='editar_programa'),
]
