from django.db import models

# Create your models here.
#tabla proyectos
class ProyectoDb(models.Model):
    nombreP = models.CharField(max_length=100,verbose_name="Nombre")
    descripcionP = models.TextField(verbose_name='Descripcion',max_length=400,default='')
    fechaI = models.DateField(verbose_name='Fecha Creacion',null=False,blank=False)
    fechaF = models.DateField(verbose_name='Fecha Fin',null=True,blank=True)     
    estado = models.BooleanField(default=False)
    class Meta:
        db_table="Proyectos"
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombreP
#tabla usuarios
class UsuarioDb(models.Model):
    nombreU = models.CharField(max_length=50,verbose_name="Nombre")
    email = models.EmailField(max_length=30,verbose_name="Email")
    telefono=models.CharField(max_length=10,verbose_name='Telefono') 
    class Meta:
        db_table="Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.nombreU
#tabla tareas
class TareaDb(models.Model):
    nombreT = models.CharField(max_length=100,verbose_name="Nombre")
    fecha_inicio = models.DateField(verbose_name='Fecha Inicia')
    fecha_fin = models.DateField(verbose_name='Fecha Fin')
    proyecto_fk = models.ForeignKey(ProyectoDb, on_delete=models.CASCADE,verbose_name='Proyecto',related_name='tareas')    
    done = models.BooleanField(default=False)    
    class Meta:
        db_table="Tareas"
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.nombreT
#tabla -usuarios-tareas
class UsuarioTareaDb(models.Model):
    usuario_fk = models.ForeignKey(UsuarioDb, on_delete=models.CASCADE,verbose_name='Usuario',related_name='tareas')
    
    tarea_fk = models.ForeignKey(TareaDb, on_delete=models.CASCADE,verbose_name='Tarea',related_name='usuarios')
    progreso = models.IntegerField(verbose_name='Progreso',null=True,blank=True)   
       
    class Meta:
        db_table="UsuarioTareas"
        verbose_name = "UsuarioTarea"
        verbose_name_plural = "UsuarioTareas"
    def __str__(self):
        return f'{self.usuario_fk}'