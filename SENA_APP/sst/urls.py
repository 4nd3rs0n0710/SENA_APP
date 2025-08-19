from django.urls import path
from . import views

app_name = 'sst'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('documentos/', views.documentos, name='documentos'),
    path('inspecciones/', views.inspecciones, name='inspecciones'),
    path('incidentes/', views.incidentes, name='incidentes'),
    path('reportes/', views.reportes_estadisticas, name='reportes'),
]

