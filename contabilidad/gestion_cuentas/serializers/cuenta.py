from rest_framework import serializers
from ..models.cuenta import Cuenta
class CuentaSerializer(serializers.ModelSerializer):
    clase_cuenta = serializers.SerializerMethodField()
    class Meta:
        model = Cuenta
        fields = ["id","codigo","nombre" , "estado", "clase_cuenta"]
        
    def get_clase_cuenta(self,obj):
        if obj.id_clase_cuenta:
            return {
                "id" : obj.id_clase_cuenta.id,
                "codigo" : obj.id_clase_cuenta.codigo,
                "nombre" : obj.id_clase_cuenta.nombre
            }    