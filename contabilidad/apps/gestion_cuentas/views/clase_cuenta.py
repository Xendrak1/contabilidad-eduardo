from rest_framework import viewsets
from ..models.clase_cuenta import ClaseCuenta
from ...configurar.models.empresa import UserEmpresa
from ..serializers.clase_cuenta import ClaseCuentaSerializer
from rest_framework.permissions import IsAuthenticated

class ClaseCuentaViewSet(viewsets.ModelViewSet):
    queryset = ClaseCuenta.objects.all()
    serializer_class = ClaseCuentaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        print("entro al view")
        user = self.request.user
        if user.is_authenticated:
            # Obtener la primera relación UserEmpresa del usuario
            user_empresa = UserEmpresa.objects.filter(user=user).first()
            
            if user_empresa:
                # Filtrar cuentas solo de esa empresa
                return ClaseCuenta.objects.filter(id_empresa=user_empresa.empresa)
        # Ninguna cuenta si no hay usuario autenticado o sin empresa asociada
        return ClaseCuenta.objects.none()
    