from rest_framework import serializers
from ..models.movimiento import Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    
    cuenta = serializers.SerializerMethodField()
    class Meta:
        model = Movimiento
        fields = ["id", "referencia","cuenta", "debe" , "haber"]
        
    def get_cuenta(self,obj):
        return{
            "id" :obj.id_cuenta.id,
            "codigo" : obj.id_cuenta.codigo,
            "nombre" : obj.id_cuenta.nombre
        }