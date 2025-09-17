from rest_framework import viewsets
from ..models.clase_cuenta import ClaseCuenta
from ..serializers.clase_cuenta import ClaseCuentaSerializer
from rest_framework.permissions import IsAuthenticated


class ClaseCuentaViewSet(viewsets.ModelViewSet):
    queryset = ClaseCuenta.objects.all()
    serializer_class = ClaseCuentaSerializer
    #permission_classes = [IsAuthenticated]