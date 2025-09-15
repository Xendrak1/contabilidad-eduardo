from rest_framework import viewsets
from ..models.movimiento import Movimiento
from ..serializers.movimiento import MovimientoSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer