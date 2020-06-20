from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

""" Creacion de las vistas con las que contara la aplicacion 
    las cuales estan clasificadas segun su CRUD al mismo tiempo
    se han importado las librerias necesarias para procesar el codigo
"""


class Inicio(TemplateView):
    template_name='index.html'

#CRUD ASIGNADO A PACIENTE
class ListadoExpediente(ListView):
    model = Expediente
    template_name='listado/listar_expediente.html'
    context_object_name='expedientes'
    queryset = Expediente.objects.all()
   
class ActualizarExpediente(UpdateView):
    model=Expediente
    template_name = 'modificables/editar_expediente.html'
    context_object_name='expedientes'
    form_class = ExpedienteForm
    success_url = reverse_lazy('clinica:listar_expediente')

class CrearExpediente(CreateView):
    model = Expediente
    form_class = ExpedienteForm
    template_name = 'clinica/crear_expediente.html'
    success_url = reverse_lazy('clinica:crear_paciente')

#CRUD ASIGNADO A PACIENTE
class ListadoPaciente(ListView):
    model = Paciente
    template_name='listado/listar_paciente.html'
    context_object_name='pacientes'
    queryset = Paciente.objects.all()
   
class ActualizarPaciente(UpdateView):
    model=Paciente
    template_name = 'modificables/editar_paciente.html'
    context_object_name='pacientes'
    form_class = PacienteForm
    success_url = reverse_lazy('clinica:listar_paciente')

class CrearPaciente(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/crear_paciente.html'
    success_url = reverse_lazy('clinica:listar_paciente')


class EliminarPaciente(DeleteView):
    model = Paciente
    success_url = reverse_lazy('clinica:listar_paciente')

#CRUD ASIGNADO A CONSULTA

class ListadoConsulta(ListView):
    model = Consulta
    template_name='listado/listar_consulta.html'
    context_object_name='consultas'
    queryset = Consulta.objects.all()

class CrearConsulta(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'clinica/crear_consulta.html'
    success_url = reverse_lazy('clinica:listar_consulta')

class ActualizarConsulta(UpdateView):
    model=Consulta
    template_name = 'modificables/editar_consulta.html'
    context_object_name='consultas'
    form_class = ConsultaForm
    success_url = reverse_lazy('clinica:listar_consulta')

class EliminarConsulta(DeleteView):
    model = Consulta
    success_url = reverse_lazy('clinica:listar_consulta')

#CRUD ASIGNADO A CITA

class ListadoCita(ListView):
    model = Cita
    template_name='listado/listar_cita.html'
    context_object_name='citas'
    queryset=Cita.objects.all()

class CrearCita(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/crear_cita.html'
    success_url = reverse_lazy('clinica:listar_cita')

class ActualizarCita(UpdateView):
    model = Cita
    template_name='modificables/editar_cita.html'
    context_object_name = 'citas'
    form_class = CitaForm
    success_url = reverse_lazy('clinica:listar_cita')

class EliminarCita(DeleteView):
    model = Cita
    success_url = reverse_lazy('clinica:listar_cita')

# CRUD ASIGNADOS A INCAPACIDAD

class ListadoIncapacidad(ListView):
    model = Incapacidad
    template_name = 'listado/listar_incapacidad.html'
    context_object_name='incapacidades'
    queryset = Incapacidad.objects.all()

class CrearIncapacidad(CreateView):
    model = Incapacidad
    form_class = IncapacidadForm
    template_name = 'clinica/crear_incapacidad.html'
    success_url = reverse_lazy('clinica:listar_incapacidad')

class EliminarIncapacidad(DeleteView):
    model = Incapacidad
    success_url = reverse_lazy('clinica:listar_incapacidad')


#CRUD ASIGNADO A MEDICOS

class ListadoMedicos(ListView):
    model = Medico
    template_name = 'listado/listar_medico.html'
    context_object_name = 'medicos'
    queryset = Medico.objects.all()

class CrearMedico(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/crear_medico.html'
    success_url = reverse_lazy('clinica:listar_medico')

class ActualizarMedico(UpdateView):
    model = Medico
    template_name='modificables/editar_medico.html'
    context_object_name = 'medicos'
    form_class = MedicoForm
    success_url = reverse_lazy('clinica:listar_medico')

class EliminarMedico(DeleteView):
    model = Medico
    success_url = reverse_lazy('clinica:listar_medico')


#CRUD ASIGNADO A ESPECIALIDADES

class ListadoEspecialidad(ListView):
    model = Especialidad
    template_name = 'listado/listar_especialidad.html'
    context_object_name = 'especialidades'
    queryset = Especialidad.objects.all()

class CrearEspecialidad(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name='clinica/crear_especialidad.html'
    success_url = reverse_lazy('clinica:listar_especialidad')

class EliminarEspecialidad(DeleteView):
    model = Especialidad
    success_url = reverse_lazy('clinica:listar_especialidad')