# Generated by Django 3.0.7 on 2020-06-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(max_length=10, verbose_name='Sexo'),
        ),
    ]