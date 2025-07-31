from django.contrib import admin
from django.urls import path, include
from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='inicio'),
    path('aprendices/', include('aprendices.urls')),
    path('instructores/', include('instructores.urls')),
]