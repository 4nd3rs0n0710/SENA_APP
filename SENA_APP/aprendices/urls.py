from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    path('editar_aprendiz/<int:id>/', views.editar_aprendiz, name='editar_aprendiz'),
]

