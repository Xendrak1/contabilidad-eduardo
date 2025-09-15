from rest_framework import viewsets
from ..models.cuenta import Cuenta
from ..serializers.cuenta import CuentaSerializer

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer