from django.shortcuts import render
from rest_framework import generics,viewsets#para las vistas
from app_proyecto.models import ProyectoDb,TareaDb
from .serializer import (
    ProyectoDbSerializer,
    TareaDbSerializer,
    UsuarioDbSerializer,
    ProyectoConTareasSerializer,
    )


# Create your views here.
class ProyectoDbAPIList(generics.ListAPIView):
    queryset = ProyectoDb.objects.all()
    serializer_class = ProyectoDbSerializer
class ProyectoConTareasAPIList(generics.ListAPIView):
    queryset = ProyectoDb.objects.all()
    serializer_class = ProyectoConTareasSerializer
class ProyectoDbAPCreate(generics.CreateAPIView):
    queryset = ProyectoDb.objects.all()
    serializer_class = ProyectoDbSerializer
class TareaDbApList(generics.ListAPIView):
    queryset = TareaDb.objects.all()
    serializer_class = TareaDbSerializer

#viewSets
class ProyectoDbAPView(viewsets.ModelViewSet):
    queryset = ProyectoDb.objects.all()
    serializer_class = ProyectoDbSerializer
class TareaDbAPView(viewsets.ModelViewSet):
    queryset = TareaDb.objects.all()
    serializer_class = TareaDbSerializer
class UsuarioDbAPView(viewsets.ModelViewSet):
    queryset = TareaDb.objects.all()
    serializer_class = UsuarioDbSerializer
