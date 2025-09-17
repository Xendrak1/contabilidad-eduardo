from rest_framework import serializers
from ..models.empresa import Empresa,UserEmpresa
from django.contrib.auth.models import User

class UserEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmpresa
        fields = ['user', 'rol', 'fecha_asociacion']

class EmpresaSerializer(serializers.ModelSerializer):
    usuarios = UserEmpresaSerializer(source='usuarioempresa_set', many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'usuarios']