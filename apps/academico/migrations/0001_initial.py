# Generated by Django 4.1.1 on 2022-09-22 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_uni', models.CharField(max_length=9)),
                ('numero_dni', models.CharField(max_length=9)),
                ('apellido_p', models.CharField(max_length=20)),
                ('apellido_m', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Alumno',
                'db_table': 'Alumnos',
                'ordering': ['apellido_p', 'apellido_m', 'nombres'],
            },
        ),
        migrations.CreateModel(
            name='CiclosAcademicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.CharField(max_length=4)),
                ('ciclo', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('tipo', models.CharField(choices=[('N', 'Normal'), ('V', 'Vacacional')], max_length=1)),
            ],
            options={
                'verbose_name': 'CiclosAcademicos',
                'db_table': 'CiclosAcademicos',
                'ordering': ['anno', 'ciclo'],
            },
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_dni', models.CharField(max_length=9)),
                ('apellido_p', models.CharField(max_length=20)),
                ('apellido_m', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Docentes',
                'db_table': 'Docentes',
                'ordering': ['apellido_p', 'apellido_m', 'nombres'],
            },
        ),
        migrations.CreateModel(
            name='SistemaEvaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema_evaluacion', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'SistemaEvaluacion',
                'db_table': 'SistemasEvaluacion',
                'ordering': ['sistema_evaluacion'],
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5)),
                ('curso', models.CharField(max_length=40)),
                ('sistema_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.sistemaevaluacion')),
            ],
            options={
                'verbose_name': 'Cursos',
                'db_table': 'Cursos',
                'ordering': ['curso', 'codigo'],
            },
        ),
    ]