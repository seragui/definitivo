# Generated by Django 3.0.7 on 2020-06-15 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('idCita', models.AutoField(primary_key=True, serialize=False)),
                ('idMedico', models.IntegerField(verbose_name='IdMedico')),
                ('idPaciente', models.IntegerField(verbose_name='IdPaciente')),
                ('idEspecialidad', models.IntegerField(verbose_name='IdEspecialidad')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.CharField(max_length=5, null=True, verbose_name='Hora')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'ordering': ['idCita'],
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('idConsulta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='FechaConsulta')),
                ('idCita', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.Cita')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ['idConsulta'],
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('idEspecialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('dui', models.CharField(max_length=10, verbose_name='DUI')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('estadoCivil', models.CharField(max_length=6, verbose_name='estadoCivil')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('fechaNaci', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.TextField(max_length=300, verbose_name='Direccion')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('altura', models.IntegerField(verbose_name='Altura')),
                ('peso', models.IntegerField(verbose_name='Peso')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
                'ordering': ['idMedico'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('expediente', models.IntegerField(verbose_name='No.Expediente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('dui', models.CharField(max_length=10, verbose_name='DUI')),
                ('sexo', models.CharField(choices=[('Masculino', 'M'), ('Femenino', 'F')], max_length=10, verbose_name='Sexo')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('estadoCivil', models.CharField(max_length=10, verbose_name='estadoCivil')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('fechaNaci', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.TextField(max_length=300, verbose_name='Direccion')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('altura', models.FloatField(verbose_name='Altura')),
                ('peso', models.FloatField(verbose_name='Peso')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['id_paciente'],
            },
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('idReferencia', models.AutoField(primary_key=True, serialize=False)),
                ('idMedico', models.IntegerField(verbose_name='IdMedico')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('lugarReferencia', models.CharField(max_length=50, verbose_name='LugarReferencia')),
                ('tipoReferencia', models.CharField(max_length=50, verbose_name='TipoReferencia')),
            ],
            options={
                'verbose_name': 'Referencia',
                'verbose_name_plural': 'Referencias',
                'ordering': ['idReferencia'],
            },
        ),
        migrations.CreateModel(
            name='Incapacidad',
            fields=[
                ('idIncapacidad', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.TextField(max_length=400, verbose_name='Motivo')),
                ('dias', models.IntegerField(verbose_name='Dias')),
                ('idConsulta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.Consulta')),
            ],
            options={
                'verbose_name': 'Incapacidad',
                'verbose_name_plural': 'Incapacidades',
                'ordering': ['idIncapacidad'],
            },
        ),
        migrations.AddField(
            model_name='consulta',
            name='idEspecialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.Especialidad'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='idMedico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='idPaciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.Paciente'),
        ),
    ]