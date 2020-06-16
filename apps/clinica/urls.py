from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns=[
    path('crear_paciente/', login_required(CrearPaciente.as_view()) ,name= 'crear_paciente'),
    path('listar_paciente/',login_required(ListadoPaciente.as_view()),name='listar_paciente'),
    path('editar_paciente/<int:pk>',ActualizarPaciente.as_view(), name = 'editar_paciente'),
    path('eliminar_paciente/<int:pk>',EliminarPaciente.as_view(),name='eliminar_paciente'),

    path('crear_consulta/', login_required(CrearConsulta.as_view()),name='crear_consulta'),
    path('listar_consulta/',login_required(ListadoConsulta.as_view()),name='listar_consulta'),
    path('editar_consulta/<int:pk>',login_required(ActualizarConsulta.as_view()),name='editar_consulta'),
    path('eliminar_consulta/<int:pk>',login_required(EliminarConsulta.as_view()),name='eliminar_consulta'),


    path('crear_cita/',login_required(CrearCita.as_view()),name='crear_cita'),
    path('listar_cita/',login_required(ListadoCita.as_view()),name='listar_cita'),
    path('editar_cita/<pk>',login_required(ActualizarCita.as_view()), name = 'editar_cita'),
    path('eliminar_cita/<pk>',login_required(EliminarCita.as_view()),name='eliminar_cita'),
]
