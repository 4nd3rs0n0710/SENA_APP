from django.contrib import admin
from django.urls import path, include
from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='inicio'),
    path('aprendices/', include('aprendices.urls')),
    path('instructores/', include('instructores.urls')),
    path('', include('programas.urls')),
]

# Personalización del pnel administrativo

admin.site.site_header = "Panel Administrativo SENA"
admin.site.site_title = "SENA APP"
admin.site.site_title = "Gestión de Aprendices"