from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Referencia)
admin.site.register(Especialidad)
admin.site.register(Cita)
admin.site.register(Incapacidad)
admin.site.register(Expediente)