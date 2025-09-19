from rest_framework import serializers
from ..models.movimiento import Movimiento
from ...gestion_cuentas.models.cuenta import Cuenta
from ...gestion_asientos.models.asiento_contable import AsientoContable

class MovimientoSerializer(serializers.ModelSerializer):
    cuenta = serializers.SerializerMethodField()
    id_cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.all(), write_only=True)
    id_asiento_contable = serializers.PrimaryKeyRelatedField(
        queryset=AsientoContable.objects.all(),
        write_only=True,
        required=False
    )    
    fecha = serializers.SerializerMethodField()
    class Meta:
        model = Movimiento
        fields = ["id", "referencia", "cuenta", "debe",
                  "haber", "id_cuenta", "id_asiento_contable", "fecha"]
        
    def get_cuenta(self,obj):
        return{
            "id" :obj.id_cuenta.id,
            "codigo" : obj.id_cuenta.codigo,
            "nombre" : obj.id_cuenta.nombre
        }
    def get_fecha(self, obj):
        # devuelve el created_at en formato ISO o personalizado
        return obj.id_asiento_contable.created_at.isoformat()    
        

            