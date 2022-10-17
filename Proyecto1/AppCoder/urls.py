from django.urls import path
from AppCoder import views
from AppCoder.views import entregables, inicio, cursos, profesores, estudiantes, procesar_formulario, procesar_formulario2, busqueda, busqueda_2, buscar, buscar_2


urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path('cursos', cursos, name="cursos"),
    path('profesores', profesores, name="profesores"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path('entregables', entregables, name="entregables"),
    path('formulario/', procesar_formulario, name="formulario"),
    path('formulario-2/', procesar_formulario2, name="formulario_2"),
    path('busqueda/', busqueda, name="busqueda"),
    path('busqueda-2/', busqueda_2, name="busqueda-2"),
    path('buscar/', buscar),
    path('buscar-2/', buscar_2),    
    ]