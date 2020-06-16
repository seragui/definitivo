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