from rest_framework import serializers
from ..models import ClaseCuenta

class ClaseCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseCuenta
        # campos que consume el api
        fields = ["id" , "codigo" , "nombre", "id_padre"]