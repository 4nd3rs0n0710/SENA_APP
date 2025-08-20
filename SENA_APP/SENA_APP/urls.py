from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings
from django.conf.urls.static import static # Importa static
from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='inicio'),
    path('aprendices/', include('aprendices.urls')),
    path('instructores/', include('instructores.urls')),
    path('programas/', include('programas.urls')),
    path('sst/', include('sst.urls', namespace='sst')),
]
# Personalización del panel administrativo

admin.site.site_header = "Panel Administrativo SENA"
admin.site.site_title = "SENA APP"
admin.site.site_title = "Gestión de Aprendices"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)