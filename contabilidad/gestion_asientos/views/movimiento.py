from rest_framework import viewsets
from ..models.movimiento import Movimiento
from ..serializers.movimiento import MovimientoSerializer
from rest_framework.permissions import IsAuthenticated

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permission_classes = [IsAuthenticated]
    