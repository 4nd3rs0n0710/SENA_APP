from django.contrib import admin
from django.urls import path, include # <--- Asegúrate de que 'include' esté aquí.
# ¡IMPORTANTE! NO DEBES poner 'from . import views' aquí.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea "incluye" todas las URL definidas en la aplicación 'aprendices'.
    # Todas las URL de tu app 'aprendices' serán manejadas por su propio urls.py.
    path('', include('aprendices.urls')), # <--- Esta es la línea clave.
]