from rest_framework import serializers
from ..models.clase_cuenta import ClaseCuenta
from ...configurar.models.empresa import UserEmpresa

class ClaseCuentaSerializer(serializers.ModelSerializer):
    # id_padre solo esta disponible para lectura
    id_padre = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ClaseCuenta
        # campos que consume el api
        fields = ["id" , "codigo" , "nombre", "id_padre","id_empresa"]

    
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