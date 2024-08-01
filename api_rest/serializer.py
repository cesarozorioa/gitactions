from rest_framework import serializers
from app_proyecto.models import ProyectoDb,TareaDb,UsuarioDb

class ProyectoDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoDb
        fields = '__all__'
    
class TareaDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaDb
        fields = '__all__'

class UsuarioDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDb
        fields = '__all__'

class ProyectoConTareasSerializer(serializers.ModelSerializer):
    tareas = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProyectoDb
        fields = '__all__'