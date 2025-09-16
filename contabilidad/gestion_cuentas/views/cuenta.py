from rest_framework import viewsets
from ..models.cuenta import Cuenta
from ..serializers.cuenta import CuentaSerializer
from rest_framework.permissions import IsAuthenticated

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]