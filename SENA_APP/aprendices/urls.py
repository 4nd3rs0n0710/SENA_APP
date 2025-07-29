from django.urls import path
from . import views

urlpatterns = [
    path('aprendices/', views.aprendices, name='lista_aprendices'),
]


