from django.urls import path
from . import views
app_name = 'instructores' 

urlpatterns = [
    path('', views.instructores, name='lista_instructores'),
]