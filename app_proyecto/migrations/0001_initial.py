# Generated by Django 5.0.6 on 2024-06-21 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectoDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcionP', models.TextField(default='', max_length=400, verbose_name='Descripcion')),
                ('fechaI', models.DateField(verbose_name='Fecha Creacion')),
                ('fechaF', models.DateField(blank=True, null=True, verbose_name='Fecha Fin')),
                ('estado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'db_table': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='UsuarioDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreU', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='TareaDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreT', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha Inicia')),
                ('fecha_fin', models.DateField(verbose_name='Fecha Fin')),
                ('done', models.BooleanField(default=False)),
                ('proyecto_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_proyecto.proyectodb', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'db_table': 'Tareas',
            },
        ),
        migrations.CreateModel(
            name='UsuarioTareaDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progreso', models.BigIntegerField(blank=True, null=True, verbose_name='Progreso')),
                ('tarea_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_proyecto.tareadb', verbose_name='Tarea')),
                ('usuario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_proyecto.usuariodb', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'UsuarioTarea',
                'verbose_name_plural': 'UsuarioTareas',
                'db_table': 'UsuarioTareas',
            },
        ),
    ]
