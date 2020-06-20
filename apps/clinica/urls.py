from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

"""Asignacion de la rutas de la aplicacion
"""

urlpatterns =[
    path('crear_expediente/', login_required(CrearExpediente.as_view()) ,name= 'crear_expediente'),
    path('listar_expediente/',login_required(ListadoExpediente.as_view()),name='listar_expediente'),
    path('editar_expediente/<pk>',login_required(ActualizarExpediente.as_view()), name = 'editar_expediente'),


    path('crear_paciente/', login_required(CrearPaciente.as_view()),name= 'crear_paciente'),
    path('listar_paciente/',login_required(ListadoPaciente.as_view()),name='listar_paciente'),
    path('editar_paciente/<int:pk>',login_required(ActualizarPaciente.as_view()), name = 'editar_paciente'),
    path('eliminar_paciente/<int:pk>',login_required(EliminarPaciente.as_view()),name='eliminar_paciente'),

    path('crear_consulta/', login_required(CrearConsulta.as_view()),name='crear_consulta'),
    path('listar_consulta/',login_required(ListadoConsulta.as_view()),name='listar_consulta'),
    path('editar_consulta/<int:pk>',login_required(ActualizarConsulta.as_view()),name='editar_consulta'),
    path('eliminar_consulta/<int:pk>',login_required(EliminarConsulta.as_view()),name='eliminar_consulta'),


    path('crear_cita/',login_required(CrearCita.as_view()),name='crear_cita'),
    path('listar_cita/',login_required(ListadoCita.as_view()),name='listar_cita'),
    path('editar_cita/<pk>',login_required(ActualizarCita.as_view()), name = 'editar_cita'),
    path('eliminar_cita/<pk>',login_required(EliminarCita.as_view()),name='eliminar_cita'),

    path('crear_incapacidad/',login_required(CrearIncapacidad.as_view()),name= 'crear_incapacidad'),
    path('listar_incapacidad/',login_required(ListadoIncapacidad.as_view()),name='listar_incapacidad'),
    path('eliminar_incapacidad/<pk>',login_required(EliminarIncapacidad.as_view()),name='eliminar_incapacidad'),

    path('crear_medico/', login_required(CrearMedico.as_view()) ,name= 'crear_medico'),
    path('listar_medico/',login_required(ListadoMedicos.as_view()),name='listar_medico'),
    path('editar_medico/<int:pk>',login_required(ActualizarMedico.as_view()), name = 'editar_medico'),
    path('eliminar_medico/<int:pk>',login_required(EliminarMedico.as_view()),name='eliminar_medico'),  

    path('crear_especialidad/', login_required(CrearEspecialidad.as_view()) ,name= 'crear_especialidad'),
    path('listar_especialidad/',login_required(ListadoEspecialidad.as_view()),name='listar_especialidad'),
    path('eliminar_especialidad/<pk>',login_required(EliminarEspecialidad.as_view()),name='eliminar_especialidad'),
      
]
