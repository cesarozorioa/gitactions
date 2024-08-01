from django.urls import path
from .views import indexHome,tareasView,listaProyectos,listaProyectosId,actualizar_tarea
urlpatterns = [    
    path('', indexHome),
    path('proyectos/<int:id>', tareasView),
    path('api/proyectos/', listaProyectos),
    path('api/proyectosid/<int:id>', listaProyectosId),
    path('actualizar-tarea/<int:item_id>/', actualizar_tarea, name='actualizar_tarea')
]