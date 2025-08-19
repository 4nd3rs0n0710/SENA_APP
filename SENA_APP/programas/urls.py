# programas/urls.py
from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.programas, name='lista_programas'),
    path('crear/', views.crear_programa, name='crear_programa'),
    path('<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
    path('<int:programa_id>/editar/', views.editar_programa, name='editar_programa'),
]
