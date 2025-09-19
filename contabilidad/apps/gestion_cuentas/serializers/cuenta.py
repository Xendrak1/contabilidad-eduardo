from rest_framework import serializers
from ..models.cuenta import Cuenta
from ...configurar.models.empresa import UserEmpresa



class CuentaSerializer(serializers.ModelSerializer):
    clase_cuenta = serializers.SerializerMethodField()
    class Meta:
        model = Cuenta
        fields = ["id","codigo","nombre" , "estado", "clase_cuenta","id_empresa"]
        extra_kwargs = {
            "id_empresa": {"read_only": True}  # <--- ya no será obligatorio
        }
        
    def get_clase_cuenta(self,obj):
        if obj.id_clase_cuenta:
            return {
                "id" : obj.id_clase_cuenta.id,
                "codigo" : obj.id_clase_cuenta.codigo,
                "nombre" : obj.id_clase_cuenta.nombre
            }    
    
    def create(self, validated_data):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("Usuario no autenticado")

        # Obtener la empresa del usuario
        user_empresa = UserEmpresa.objects.filter(user=request.user).first()
        if not user_empresa:
            raise serializers.ValidationError("El usuario no tiene empresa asociada")

        # Asignar automáticamente la empresa
        validated_data["id_empresa"] = user_empresa.empresa
        return super().create(validated_data)        
    

    