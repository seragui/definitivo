# Generated by Django 3.0.7 on 2020-06-20 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('idExpediente', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Edad')),
                ('sexo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sexo')),
                ('estado', models.CharField(blank=True, max_length=200, null=True, verbose_name='Estado')),
                ('altura', models.FloatField(blank=True, null=True, verbose_name='Altura')),
                ('peso', models.FloatField(blank=True, null=True, verbose_name='Peso')),
                ('temperatura', models.FloatField(blank=True, null=True, verbose_name='Temperatura')),
                ('presart', models.CharField(blank=True, max_length=200, null=True, verbose_name='Presión Arterial')),
                ('enfermedadeshe', models.TextField(blank=True, max_length=400, null=True, verbose_name='Enfermedades Hereditarias')),
                ('alergias', models.TextField(blank=True, max_length=400, null=True, verbose_name='Alergias')),
                ('obserpsi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observaciones Psicologicas')),
            ],
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='expediente',
        ),
        migrations.AddField(
            model_name='paciente',
            name='idExpediente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.Expediente'),
        ),
    ]
