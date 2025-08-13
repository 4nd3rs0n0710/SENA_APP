# SENA_App/aprendices/urls.py
from django.urls import path
from . import views

# El 'app_name' es importante para evitar conflictos con otras aplicaciones
# y poder referenciar las URLs con el formato 'app_name:nombre_url'.
app_name = 'aprendices' 

urlpatterns = [
    # URL para la página de inicio
    path('', views.inicio, name='inicio'),

    # URLs para aprendices
    path('lista/', views.lista_aprendices, name='lista_aprendices'),
    path('agregar_aprendiz/', views.agregar_aprendiz, name='agregar_aprendiz'),
    path('aprendiz/<int:aprendiz_id>/', views.detalle_aprendiz, name='detalle_aprendiz'),
    path('editar/<int:aprendiz_id>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('eliminar/<int:aprendiz_id>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
    
    # URLs para cursos
    path('lista_cursos/', views.lista_cursos, name='lista_cursos'),
    path('lista_cursos/curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    
    # ... otras URLs
]
