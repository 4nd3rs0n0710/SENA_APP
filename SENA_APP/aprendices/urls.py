from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('aprendices/', views.lista_aprendices, name='lista_aprendices'),
    path('aprendices/editar/<int:aprendiz_id>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('aprendices/eliminar/<int:aprendiz_id>/', views.eliminar_aprendiz, name='eliminar_aprendiz'), # <--- ¡Nueva URL!
    # Agrega aquí cualquier otra URL que sea específica de tu aplicación 'aprendices'.
]


