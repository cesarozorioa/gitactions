from django.contrib import admin
from  .models import ProyectoDb,UsuarioDb,TareaDb,UsuarioTareaDb
# Register your models here.
admin.site.site_header="Administración de Proyectos"
admin.site.index_title="Proyectos y tareas"
class ProyectoTareas(admin.TabularInline):
    model = TareaDb
    extra = 1

@admin.register(ProyectoDb)
class ProyectoAdmin(admin.ModelAdmin):
    # agregamos los campos
    fields = ['nombreP','descripcionP','fechaI','fechaF','estado']
    list_display = ['nombreP','descripcionP','fechaI','fechaF','estado']
    list_filter = ['fechaI','estado']
    search_fields = ['nombreP']
    search_help_text = 'Busqueda por Nombre'
    ordering = ['fechaI']
    inlines = [ProyectoTareas]
@admin.register(TareaDb)
class TareaAdmin(admin.ModelAdmin):
    fields = ['nombreT', 'fecha_inicio',
              'fecha_fin','proyecto_fk','done']
    list_display = ['nombreT', 'fecha_inicio',
                    'fecha_fin', 'proyecto_fk','done']
    list_filter = ['proyecto_fk']
    search_fields = ['nombreT']
    search_help_text = 'Busqueda por Nombre'
    ordering = ['proyecto_fk']
@admin.register(UsuarioDb)   
class UsuarioAdmin(admin.ModelAdmin):
    fields = ['nombreU','email','telefono']
    list_display = ['nombreU']
    list_filter = ['email']
@admin.register(UsuarioTareaDb)
class UsuarioTareaAdmin(admin.ModelAdmin):
    fields = ['usuario_fk','tarea_fk','progreso']
    list_display = ['usuario_fk','tarea_fk','progreso']
    list_filter = ['tarea_fk']
