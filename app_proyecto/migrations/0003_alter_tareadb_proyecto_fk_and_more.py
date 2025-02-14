# Generated by Django 5.0.6 on 2024-06-21 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0002_alter_usuariotareadb_progreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareadb',
            name='proyecto_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='app_proyecto.proyectodb', verbose_name='Proyecto'),
        ),
        migrations.AlterField(
            model_name='usuariotareadb',
            name='tarea_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='app_proyecto.tareadb', verbose_name='Tarea'),
        ),
        migrations.AlterField(
            model_name='usuariotareadb',
            name='usuario_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='app_proyecto.usuariodb', verbose_name='Usuario'),
        ),
    ]
