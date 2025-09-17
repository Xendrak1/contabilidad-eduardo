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
        if self.request.user.is_authenticated:
            user_empresa = UserEmpresa.objects.filter(user=self.request.user).first()
            if user_empresa:
                return ClaseCuenta.objects.filter(id_empresa=user_empresa.empresa)
        return ClaseCuenta.objects.all() 

   