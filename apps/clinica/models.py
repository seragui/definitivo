from django.db import models

# Create your models here.


class Paciente(models.Model):

    id_paciente = models.AutoField(primary_key=True)
    expediente = models.IntegerField('No.Expediente',blank=False, null=False)
    nombre = models.CharField('Nombre',max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    dui = models.CharField('DUI', max_length=10, blank=False,null=False)
    sexo = models.CharField('Sexo', max_length=10, blank=False, null=False)
    email = models.CharField('email',max_length=100,blank=False, null=False)
    estadoCivil = models.CharField('estadoCivil', max_length=10, blank=False,null=False)
    telefono = models.CharField('Telefono', max_length=9, blank=False,null=False)
    fechaNaci = models.DateField('Fecha de Nacimiento',blank=False,null=False)
    direccion = models.TextField('Direccion',max_length=300, blank=False,null=False)
    departamento = models.CharField('Departamento',max_length=100,blank=False,null=False)
    municipio = models.CharField('Municipio',max_length=100,blank=False,null=False)
    altura = models.FloatField('Altura',blank=False,null=False)
    peso = models.FloatField('Peso', blank=False,null=False)
    
    class Meta:
            verbose_name = 'Paciente'
            verbose_name_plural = 'Pacientes'
            ordering = ['id_paciente']

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Medico(models.Model):
    idMedico= models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    dui = models.CharField('DUI', max_length=10, blank=False,null=False)
    sexo = models.CharField('Sexo', max_length=1, blank=False, null=False)
    email = models.CharField('email',max_length=100,blank=False, null=False)
    estadoCivil = models.CharField('estadoCivil', max_length=10, blank=False,null=False)
    telefono = models.CharField('Telefono', max_length=9 ,blank=False,null=False)
    fechaNaci = models.DateField('Fecha de Nacimiento',blank=False,null=False)
    direccion = models.TextField('Direccion',max_length=300, blank=False,null=False)
    departamento = models.CharField('Departamento',max_length=100,blank=False,null=False)
    municipio = models.CharField('Municipio',max_length=100,blank=False,null=False)
    altura = models.IntegerField('Altura',blank=False,null=False)
    peso = models.IntegerField('Peso', blank=False,null=False)

    class Meta:
        verbose_name='Medico'
        verbose_name_plural= 'Medicos'
        ordering=['idMedico']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Referencia (models.Model):
    idReferencia = models.AutoField(primary_key =True)
    idMedico = models.IntegerField('IdMedico', blank=False,null=False)
    nombre= models.CharField('Nombre', max_length=50, blank=False, null=False)
    cargo = models.CharField('Cargo', max_length=50, blank=False, null=False)
    telefono = models.CharField('Telefono', max_length=50, blank=False, null=False)
    lugarReferencia = models.CharField('LugarReferencia', max_length=50,blank=False,null=False)
    tipoReferencia = models.CharField('TipoReferencia', max_length=50, blank=False, null=False)

    class Meta:
            verbose_name='Referencia'
            verbose_name_plural= 'Referencias'
            ordering=['idReferencia']
    
    def __str__(self):
        return self.nombre + ' ' + self.lugarReferencia

class Cita (models.Model):
    idCita= models.AutoField(primary_key=True)
    idMedico = models.IntegerField('IdMedico', blank=False,null=False)
    idPaciente = models.IntegerField('IdPaciente', blank=False, null=False)
    idEspecialidad = models.IntegerField('IdEspecialidad',blank = False, null= False)
    fecha = models.DateField('Fecha',blank= False, null=False)
    hora = models.CharField('Hora', max_length=5, blank=False, null=True)

    class Meta:
        verbose_name='Cita'
        verbose_name_plural='Citas'
        ordering=['idCita']

    def __str__(self):
        st = str(self.idCita)
        return st

class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=40, blank =False, null=False)

    class Meta: 
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Consulta (models.Model):
    idConsulta = models.AutoField(primary_key=True)
    idMedico = models.ForeignKey(Medico, null=True, on_delete=models.SET_NULL)
    idPaciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    idEspecialidad = models.ForeignKey(Especialidad , null=True, on_delete=models.SET_NULL)
    idCita = models.ForeignKey(Cita, null=True, on_delete=models.SET_NULL,blank=True)
    fecha= models.DateField('FechaConsulta', blank=False, null=False)

    class Meta:
            verbose_name='Consulta'
            verbose_name_plural= 'Consultas'
            ordering=['idConsulta']
    
    def __str__(self):
        st = str(self.idConsulta) +' '+str(self.idPaciente)
        return st

class Incapacidad(models.Model):
    idIncapacidad = models.AutoField(primary_key=True)
    motivo = models.TextField('Motivo',max_length=400, blank=False, null=False)
    dias= models.IntegerField('Dias',blank=False, null=False)
    idConsulta = models.ForeignKey(Consulta, null= True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Incapacidad'
        verbose_name_plural = 'Incapacidades'
        ordering = ['idIncapacidad'] 

    def __str__(self):
        st = str(self.idConsulta) +' '+str(self.idIncapacidad)
        return st

