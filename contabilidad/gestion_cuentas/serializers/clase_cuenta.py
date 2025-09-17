from rest_framework import serializers
from ..models.clase_cuenta import ClaseCuenta

class ClaseCuentaSerializer(serializers.ModelSerializer):
    # id_padre solo esta disponible para lectura
    id_padre = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ClaseCuenta
        # campos que consume el api
        fields = ["id" , "codigo" , "nombre", "id_padre"]