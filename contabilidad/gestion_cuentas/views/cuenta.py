from rest_framework import viewsets
from ..models.cuenta import Cuenta
from ..serializers.cuenta import CuentaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class CuentaViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    #permission_classes = [IsAuthenticated]