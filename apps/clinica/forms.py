from django import forms
from .models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields ='__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields ='__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

        labels = {
            'idMedico' : 'Medico',
            'idPaciente' : 'Paciente',
            'idEspecialidad' : 'Especialidad',
            'idCita' : 'idCita',
            'fecha':'Fecha de Consulta',
            
        }

        widgets = {
            'idMedico': forms.Select(attrs={'class':'form-control'}),
            'idPaciente' : forms.Select(attrs={'class':'form-control'}),
            'idEspecialidad' : forms.Select(attrs={'class':'form-control'}),
            'idCita' : forms.Select(attrs={'class':'form-control'}),
            'fecha' : forms.DateInput(attrs={'class': 'datetime-input'}),
        }

class IncapacidadForm(forms.ModelForm):
    class Meta:
        model = Incapacidad
        fields = '__all__'

        labels = {
            'motivo' : 'Motivo',
            'dias' : 'Dias a autorizar',
            'idConsulta' : 'idConsulta',
        }

        widgets ={
            'motivo': forms.Textarea(attrs={'class':'form-control'}),
            'dias' : forms.TextInput(attrs={'class':'form-control'}),
            'idConsulta' : forms.Select(attrs={'class':'form-control'}),
        }
