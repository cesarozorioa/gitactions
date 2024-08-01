from django.urls import path
from rest_framework.routers import DefaultRouter    
from .views import (
    ProyectoDbAPIList,
    TareaDbApList,
    ProyectoDbAPCreate,
    ProyectoDbAPView,
    TareaDbAPView,
    UsuarioDbAPView,
    ProyectoConTareasAPIList
    )
router = DefaultRouter()
router.register('proyectosv',ProyectoDbAPView,basename='proyectosv')
router.register('tareasv',TareaDbAPView,basename='tareasv')
router.register('usuariosv',UsuarioDbAPView,basename='usuariosv')

urlpatterns = [    
    path('lista-proyectos/', ProyectoDbAPIList.as_view(),name='lista_proyectos'),
    path('proyecto-tareas/', ProyectoConTareasAPIList.as_view(),name='proyecto_tareas'),
    path('lista-tareas/',TareaDbApList.as_view(),name='lista_tareas'),
    path('crea-proyecto/',ProyectoDbAPCreate.as_view(),name='crea_proyecto')  
]
urlpatterns += router.urls