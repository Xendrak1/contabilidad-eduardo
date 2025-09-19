from rest_framework import viewsets
from ...configurar.models.empresa import UserEmpresa
from ..models.cuenta import Cuenta
from rest_framework.response import Response
from ..serializers.cuenta import CuentaSerializer
from rest_framework.permissions import IsAuthenticated
from ...gestion_asientos.models.movimiento import Movimiento
from ...gestion_asientos.serializers.movimiento import MovimientoSerializer
from rest_framework.decorators import action



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
    
    @action(detail=True, methods=['get'])
    def movimientos(self, request, pk=None):
        """
        GET /cuentas/{id}/movimientos/
        Devuelve los movimientos asociados a la cuenta
        """
        try:
            cuenta = self.get_object()  # Obtiene la cuenta según pk
        except Cuenta.DoesNotExist:
            return Response({"detail": "Cuenta no encontrada"}, status=404)

        movimientos = Movimiento.objects.filter(id_cuenta=cuenta.id)
        serializer = MovimientoSerializer(movimientos, many=True)
        
        return Response(serializer.data)
