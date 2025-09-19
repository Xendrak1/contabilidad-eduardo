from rest_framework import serializers
from ..models import AsientoContable,Movimiento
from .movimiento import MovimientoSerializer

class AsientoContableSerializer(serializers.ModelSerializer):
    movimientos = MovimientoSerializer(many=True,required=False,allow_empty=True)
    
    class Meta:
        model = AsientoContable
        fields =["id" , "descripcion" ,"movimientos", "estado"]
    # aqui se esta creando los mov de un asiento
    def create(self, validated_data):
        
        movimientos_data = validated_data.pop("movimientos", [])  # por defecto lista vacía
        asiento = AsientoContable.objects.create(**validated_data)

        # solo crea movimientos si hay datos
        for mov_data in movimientos_data:
            Movimiento.objects.create(id_asiento_contable=asiento, **mov_data)

        return asiento