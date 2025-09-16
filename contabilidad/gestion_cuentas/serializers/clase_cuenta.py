from rest_framework import serializers
from ..models.clase_cuenta import ClaseCuenta

class ClaseCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseCuenta
        # campos que consume el api
        fields = ["id" , "codigo" , "nombre", "id_padre"]