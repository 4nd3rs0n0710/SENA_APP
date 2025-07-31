# SENA_App/aprendices/urls.py
from django.urls import path
from . import views

app_name = 'aprendices' # Buena práctica para namespacing

urlpatterns = [
    # La ruta vacía aquí se resolverá como '/aprendices/' gracias al include en el urls.py principal.
    path('', views.lista_aprendices, name='lista_aprendices'),
    path('editar/<int:aprendiz_id>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('eliminar/<int:aprendiz_id>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
]
