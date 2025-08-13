from django.urls import path
from . import views
from .views import InstructorFormView, InstructorUpdateView # Las vistas basadas en clases que estabas usando

app_name = 'instructores'

urlpatterns = [
    # Esta línea estaba mal, la corregimos para que llame a la vista 'instructores'
    path('', views.instructores, name='lista_instructores'), 
    
    path('instructor/<int:id>/', views.detalle_instructor, name='detalle_instructor'),
    path('crear_instructor/', InstructorFormView.as_view(), name='crear_instructor'),
    path('editar_instructor/<int:pk>/', InstructorUpdateView.as_view(), name='editar_instructor'),
]