from rest_framework import viewsets
from ...configurar.models.empresa import UserEmpresa
from ..models.cuenta import Cuenta
from ..serializers.cuenta import CuentaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class CuentaViewSet(viewsets.ModelViewSet):
    
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Obtener la primera relación UserEmpresa del usuario
            user_empresa = UserEmpresa.objects.filter(user=user).first()
            if user_empresa:
                # Filtrar cuentas solo de esa empresa
                return Cuenta.objects.filter(id_empresa=user_empresa.empresa)
        # Ninguna cuenta si no hay usuario autenticado o sin empresa asociada
        return Cuenta.objects.none()
