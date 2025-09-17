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
        if self.request.user.is_authenticated:
            user_empresa = UserEmpresa.objects.filter(user=self.request.user).first()
            if user_empresa:
                return Cuenta.objects.filter(id_empresa=user_empresa.empresa)
        return Cuenta.objects.all() 
